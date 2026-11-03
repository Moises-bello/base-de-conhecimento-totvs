---
article_id: 360061752454
category: Inspeção de Entradas (SIGAQIE)
content_hash: f337087a3cc47da93c21fb14a42c35d6caba434bc73781b061232ce3bfa244f3
fetched_at: '2026-06-28T22:42:27.118773+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Parâmetro MV_PRFOFAB
type: support-article
updated_at: '2025-09-01T14:29:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061752454-Manufatura-Linha-Protheus-SIGAQIE-Par%C3%A2metro-MV-PRFOFAB
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17792171225623)**Tempo aproximado para leitura:**00:00:50 min**  
**Dúvida**Qual a utilização do parâmetro **MV\_PRFOFAB - Seleciona índices de qualidade legado**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**O parâmetro **MV\_PRFOFAB** será utilizado na geração do índice de qualidade pela rotina **QIEA230 - Geração do Índice de Qualidade**.  
Se o parâmetro estiver ativo, com conteúdo igual à **T - True**, será analisando o conteúdo do campo **A5\_FABR - Fabricante**, caso contrário, este campo será desconsiderado na geração do índice de qualidade.  
  
**Importante**  
Independente do conteúdo deste parâmetro, é obrigatório o preenchimento do campo **A5\_FABREV -** **Fab/Rev/Perm** da rotina **MATA061 - Atualização Produto x Fornecedor**, que irá registrar a informação no campo **A5\_FABR**, para produtos que serão inspecionados pelo **Qualidade**.  
  
**Observação**  
A partir da release **12.1.2410,** com a **alteração expedida no pacote [DMANQUALI-11018](https://tdn.totvs.com/display/PROT/24372422+DMANQUALI-11018+DT+SigaQIE+-+MV_PRFOFAB) em 29.08.2025**, o parâmetro **MV\_PRFOFAB** não é mais validado no módulo **SIGAQIE - Inspeção de Entradas**.
