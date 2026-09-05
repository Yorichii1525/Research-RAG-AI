import React, { useState } from 'react';
import axios from 'axios';
import { UploadCloud, CheckCircle, AlertCircle, Loader2, FileText } from 'lucide-react';

const BACKEND_URL = "https://research-rag-ai.onrender.com";

export default function FileUpload({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [status, setStatus] = useState(null);

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) return;

    setUploading(true);
    setStatus(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await axios.post(`${BACKEND_URL}/api/documents/upload`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      setStatus({ type: 'success', text: `Uploaded "${file.name}" (${res.data.data.total_pages} pages, ${res.data.data.total_chunks} chunks)` });
      setFile(null);
      if (onUploadSuccess) onUploadSuccess(res.data.data);
    } catch (err) {
      const errorDetail = err.response?.data?.detail || err.message || 'Failed to upload PDF.';
      setStatus({ type: 'error', text: errorDetail });
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg">
      <h3 className="font-semibold text-sm mb-3 flex items-center gap-2 text-slate-200">
        <FileText className="text-blue-400" size={18} /> Upload Research PDF
      </h3>

      <form onSubmit={handleUpload} className="space-y-3">
        <label className="flex flex-col items-center justify-center border-2 border-dashed border-slate-700 hover:border-blue-500 bg-slate-950/50 hover:bg-slate-900 rounded-lg p-6 cursor-pointer transition-all">
          <UploadCloud className="text-slate-400 mb-2" size={32} />
          <span className="text-xs font-medium text-slate-300">
            {file ? file.name : 'Click or Drag PDF file here'}
          </span>
          <span className="text-[10px] text-slate-500 mt-1">PDF documents only</span>
          <input
            type="file"
            accept=".pdf"
            className="hidden"
            onChange={(e) => setFile(e.target.files[0])}
          />
        </label>

        {file && (
          <button
            type="submit"
            disabled={uploading}
            className="w-full bg-blue-600 hover:bg-blue-500 disabled:opacity-50 text-white font-medium text-xs py-2 px-4 rounded-lg flex items-center justify-center gap-2 transition-all"
          >
            {uploading ? (
              <>
                <Loader2 className="animate-spin" size={14} /> Processing PDF & Vectors...
              </>
            ) : (
              'Ingest & Process Document'
            )}
          </button>
        )}
      </form>

      {status && (
        <div className={`mt-3 p-3 rounded-lg text-xs flex items-start gap-2 ${status.type === 'success' ? 'bg-emerald-950/50 border border-emerald-800 text-emerald-300' : 'bg-red-950/50 border border-red-800 text-red-300'}`}>
          {status.type === 'success' ? <CheckCircle size={14} className="mt-0.5 shrink-0" /> : <AlertCircle size={14} className="mt-0.5 shrink-0" />}
          <span className="break-words">{status.text}</span>
        </div>
      )}
    </div>
  );
}
