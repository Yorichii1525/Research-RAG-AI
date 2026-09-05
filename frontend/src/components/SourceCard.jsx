import React from 'react';
import { FileText, BookOpen } from 'lucide-react';

export default function SourceCard({ source }) {
  return (
    <div className="bg-slate-800/80 border border-slate-700/80 rounded-lg p-3 text-xs text-slate-300">
      <div className="flex items-center gap-2 mb-1.5 font-medium text-slate-200">
        <FileText size={14} className="text-blue-400" />
        <span className="truncate">{source.filename}</span>
        <span className="ml-auto bg-blue-500/20 text-blue-300 px-2 py-0.5 rounded text-[10px] flex items-center gap-1">
          <BookOpen size={10} /> Page {source.page}
        </span>
      </div>
      <p className="italic text-slate-400 line-clamp-3">"{source.content}"</p>
    </div>
  );
}