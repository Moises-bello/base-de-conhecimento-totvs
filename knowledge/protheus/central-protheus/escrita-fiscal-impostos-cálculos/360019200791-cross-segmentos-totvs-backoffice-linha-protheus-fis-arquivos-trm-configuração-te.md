---
article_id: 360019200791
category: Escrita Fiscal - Impostos - Cálculos
content_hash: ce7038bbfc7dd2950e9a7be000ad5f8013fd7559d7e7722c6fae85a0d883857c
fetched_at: '2026-06-28T22:39:30.447670+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Arquivos TRM Configuração
  - Termo de Abertura e Encerramento Livros Fiscais'
type: support-article
updated_at: '2023-04-25T19:08:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019200791--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Arquivos-TRM-Configura%C3%A7%C3%A3o-Termo-de-Abertura-e-Encerramento-Livros-Fiscais
---

**Dúvida**Como configurar os arquivos TRM no Protheus para que seja gerado os livros de abertura e encerramento do período  
  
**Ambiente**  
Protheus - Livros Fiscais – A partir da versão 11.80]  
  
**Solução**

Será necessário baixar os arquivos .TRM e configurar nos parâmetros os Arquivos de Extensão TRM, para que ele busque os arquivos que estão na pasta system.  
  
MV\_LENTAB - (Arq de Termo de Abertura do Livro de Registro de Entradas) = LENTAB.TRM  
MV\_LENTEN - (Arq de Termo de Encerramento Livro de Registro de Entradas)= LENTEN.TRM  
MV\_LISSAB - (Arq de Termo de Abertura do Livro de Registro de ISS)= LISSAB.TRM  
MV\_LISSEN - (Arq de Termo de Encerramento do Livro de Registro de ISS)= LISSEN.TRM  
MV\_LMOD3AB - (Arq do Termo de Abert do Livro de Reg de Cont de Estoq e Prod)= LMOD3AB.TRM  
MV\_LMOD3EN - (Arq do Termo de Enc do Livro de Reg de Contr. de Estoq e Prod)= LMOD3EN.TRM  
MV\_LMOD7AB - (Arq do Termo de Abertura do Livro de Registro de Inventário)= LMOD7AB.TRM  
MV\_LMOD7EN - (Arq do Termo de Enc do Livro de Reg de Inventário)= LMOD7EN.TRM  
MV\_LMOD8AB - (Arq do Termo de Abertura do Livro de Reg de Apur de IPI)= LMOD8AB.TRM  
MV\_LMOD8EN - (Arq do Termo de Enc do Livro de Reg de Apur de IPI)= LMOD8EN.TRM  
MV\_LMOD9AB - (Arq do Termo de Abertura do Livro de Reg de Apur de ICMS)= LMOD9AB.TRM  
MV\_LMOD9EN - (Arq do Termo de Enc do Livro de Reg de Apuração de ICMS)= LMOD9EN.TRM  
MV\_LSAIAB - (Arq de Termo de Abertura do Livro de Registro de Saídas)= MOD2PR.TRM        
MV\_LSAIEN - (Arq de Termo de Encerramento do Livro de Registro de Saídas)= LSAIEN.TRM
