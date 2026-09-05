import React, { useState } from 'react';
import axios from 'axios';
import { Send, Bot, User, Loader2 } from 'lucide-react';
import SourceCard from './SourceCard';

export default function ChatWindow() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim() || loading) return;

    const userMessage = { role: 'user', content: input };
    setMessages((prev) => [...prev, userMessage]);
    const currentInput = input;
    setInput('');
    setLoading(true);

    try {
      const res = await axios.post('http://127.0.0.1:8000/api/chat', {
        question: currentInput
      });

      const botMessage = {
        role: 'assistant',
        content: res.data.answer,
        sources: res.data.sources
      };
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      const errorText = err.response?.data?.detail || err.message || 'Error communicating with ResearchAI backend.';
      const errorMessage = {
        role: 'assistant',
        content: errorText,
        sources: []
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-[600px] bg-slate-900 text-slate-100 rounded-xl border border-slate-800 shadow-xl overflow-hidden">
      <div className="bg-slate-950 p-4 border-b border-slate-800 flex items-center gap-3">
        <Bot className="text-blue-400" size={22} />
        <div>
          <h2 className="font-semibold text-sm">ResearchAI Assistant</h2>
          <p className="text-[11px] text-slate-400">Grounded MMR Retrieval with Source Citations</p>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.length === 0 && (
          <div className="h-full flex flex-col items-center justify-center text-slate-500 text-xs gap-2">
            <Bot size={36} className="text-slate-600" />
            <span>Upload a document and ask a research question...</span>
          </div>
        )}

        {messages.map((msg, idx) => (
          <div key={idx} className={`flex gap-3 ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            {msg.role === 'assistant' && (
              <div className="w-7 h-7 rounded-full bg-blue-600/20 text-blue-400 flex items-center justify-center shrink-0 mt-1">
                <Bot size={16} />
              </div>
            )}

            <div className={`max-w-[85%] space-y-2 ${msg.role === 'user' ? 'bg-blue-600 text-white rounded-2xl rounded-tr-none px-4 py-2.5 text-xs font-medium' : 'bg-slate-800/90 border border-slate-700/60 rounded-2xl rounded-tl-none p-4 text-xs text-slate-200'}`}>
              <p className="whitespace-pre-wrap leading-relaxed">{msg.content}</p>

              {msg.sources && msg.sources.length > 0 && (
                <div className="mt-3 pt-3 border-t border-slate-700/60">
                  <p className="text-[10px] font-semibold text-slate-400 mb-2 uppercase tracking-wider">Source Citations</p>
                  <div className="grid grid-cols-1 gap-2">
                    {msg.sources.map((src, sIdx) => (
                      <SourceCard key={sIdx} source={src} />
                    ))}
                  </div>
                </div>
              )}
            </div>

            {msg.role === 'user' && (
              <div className="w-7 h-7 rounded-full bg-slate-700 text-slate-300 flex items-center justify-center shrink-0 mt-1">
                <User size={16} />
              </div>
            )}
          </div>
        ))}

        {loading && (
          <div className="flex items-center gap-2 text-slate-400 text-xs">
            <Loader2 className="animate-spin text-blue-400" size={16} />
            <span>Searching vector database & generating answer...</span>
          </div>
        )}
      </div>

      <form onSubmit={handleSend} className="p-3 bg-slate-950 border-t border-slate-800 flex gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question about your uploaded research documents..."
          className="flex-1 bg-slate-900 border border-slate-700/80 rounded-lg px-4 py-2 text-xs text-slate-100 focus:outline-none focus:border-blue-500 transition-all"
        />
        <button
          type="submit"
          disabled={loading || !input.trim()}
          className="bg-blue-600 hover:bg-blue-500 disabled:opacity-50 text-white px-4 py-2 rounded-lg flex items-center gap-2 transition-all font-medium text-xs"
        >
          <Send size={14} /> Send
        </button>
      </form>
    </div>
  );
}
