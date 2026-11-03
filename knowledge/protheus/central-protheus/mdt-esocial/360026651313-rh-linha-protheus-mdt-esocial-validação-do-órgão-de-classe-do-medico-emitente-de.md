---
article_id: 360026651313
category: MDT - eSocial
content_hash: fa02e24ebf320a6a9882c8f353884fcd340e20d7fe810b1620497cd2f2058cef
fetched_at: '2026-06-28T22:44:29.409862+00:00'
product: protheus
section_id: 360004428991
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - Validação do Órgão de Classe do medico
  emitente de atestado
type: support-article
updated_at: '2025-08-05T17:18:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026651313-RH-Linha-Protheus-MDT-eSocial-Valida%C3%A7%C3%A3o-do-%C3%93rg%C3%A3o-de-Classe-do-medico-emitente-de-atestado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27595888091671)**Tempo aproximado para leitura: 00:01:00 min **Dúvida**Ao realizar um lançamento um atestado Médico integrado com Gestão de Pessoal (SIGAGPE), é apresentada mensagem informando que os campos Órg.Classe (**TNP\_ENTCLA)** e Ent. Classe (**R8\_IDEOC)** estão preenchidos de forma inválida.   
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Conforme layout do eSocial, o preenchimento desses campos são obrigatórios para geração dos eventos S-2230 e S-2210. Para ajustar, acesse a rotina **SESMT/Usuar.aten. (MDTA070)** localizada no Módulo 35 (SIGAMDT) no caminho: Atualizações - Sesmt - Sesmt/usuar.aten ou emitente de atestado no caminho: Atualizações - Atendimento Médico - Médico Emitente de Atestado **(****MDTA680).**Para saber a diferença entre as rotinas Usuar.aten. e  Emitente de Atestado acesse: [MP - MDT - Qual a diferença entre a rotina SESMT/Usuar.aten. (MDTA070) e a rotina Emitentes de Atestados (MDTA680) no modulo medicina e segurança do trabalho (SIGAMDT)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056925334-MP-MDT-Qual-a-diferen%C3%A7a-entre-a-rotina-SESMT-Usuar-aten-MDTA070-e-a-rotina-Emitentes-de-Atestados-MDTA680-no-modulo-medicina-e-seguran%C3%A7a-do-trabalho-SIGAMDT-?source=search) **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042191433)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042191593)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042191733)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042191793)  
  
Observação**

* Se desejar que o sistema apenas emita o aviso sem bloquear a inclusão altere o parâmetro **MV\_NG2AVIS** para 0 (emite aviso).
* Se desejar desabilitar a integração do **SIGAMDT** com **TAF** altere o parâmetro **MV\_NG2ESOC** para 2.

**Saiba Mais**Para saber mais consulte os links abaixo:  
[Artigos MDT - eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial-Protheus)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)
