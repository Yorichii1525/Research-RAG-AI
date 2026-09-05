import React from 'react';
import FileUpload from './components/FileUpload';
import ChatWindow from './components/ChatWindow';
import { Sparkles } from 'lucide-react';

export default function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col">
      <header className="border-b border-slate-800 bg-slate-900/60 backdrop-blur px-6 py-4 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Sparkles className="text-blue-500" size={24} />
          <h1 className="font-bold text-base tracking-tight text-white">ResearchAI</h1>
          <span className="text-[10px] bg-blue-500/20 text-blue-300 font-semibold px-2 py-0.5 rounded-full border border-blue-500/30">RAG Assistant</span>
        </div>
        <p className="text-xs text-slate-400 hidden sm:block">FastAPI + ChromaDB + React RAG Pipeline</p>
      </header>

      <main className="flex-1 max-w-6xl w-full mx-auto p-6 grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="md:col-span-1 space-y-6">
          <FileUpload />
        </div>
        <div className="md:col-span-2">
          <ChatWindow />
        </div>
      </main>
    </div>
  );
}