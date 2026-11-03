---
article_id: 360033791133
category: Financeiro - Contas a Pagar
content_hash: cf6ce7b620749b8a03b217ee9a98e47c5fa214988e099bb8ca368865ddd774a7
fetched_at: '2026-06-28T22:38:09.978724+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP- SIGAFIN - FINA050 - Não gera INSS pessoa física
type: support-article
updated_at: '2021-04-28T15:18:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033791133-MP-SIGAFIN-FINA050-N%C3%A3o-gera-INSS-pessoa-f%C3%ADsica
---

**Ocorrência**Ao incluir um título não gera INSS para pessoa física?  
   
 **Ambiente**Microsiga Protheus – Financeiro – FINA050 – A partir da versão 8.0

**Causa**Pessoa física existe um teto para a geração um limite, acima disso não é gerado.  
   
 **Solução** **MV\_LIMINSS** – Valor Máximo do imposto a ser retido da PF ex: 642.34

O parâmetro **MV\_LIMINSS** = 642,34**(Valor Máximo do imposto a ser retido da PF)**  
  
Exemplo: Título de  10.000,00 x 11% = 1.100,00, neste caso o valor é superior ao valor máximo gerado para a Pessoa Física cadastrado no parâmetro, portanto não vai gerar no sistema e está correto.
