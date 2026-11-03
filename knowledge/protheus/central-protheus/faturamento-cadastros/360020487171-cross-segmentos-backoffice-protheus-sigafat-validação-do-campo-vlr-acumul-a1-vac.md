---
article_id: 360020487171
category: Faturamento - Cadastros
content_hash: e9abc70130d63692bf09f073b7ee8b59dc4c1e670b7d675f3d7c798f3e28a05e
fetched_at: '2026-06-28T22:38:35.404936+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT -  Validação do Campo "Vlr.
  Acumul A1_VACUM"
type: support-article
updated_at: '2025-02-20T20:10:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020487171-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Valida%C3%A7%C3%A3o-do-Campo-Vlr-Acumul-A1-VACUM
---

**Dúvida**Como o campo Valor Acumulado de Vendas no Ano **"Vlr. Acumul** **A1\_VACUM"** é validado?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.

**Solução**

O Protheus não atualiza os campos **"Vlr. Acumul** **A1\_VACUM"** e **"Nro Compras** **A1\_NROCOM"** se o módulo for o **SigaLoja** ou **Frontloja** (via RPC) e o cliente for igual a cliente padrão.

Se os campos **"Código A1\_COD"** + **"Loja A1\_LOJA"** do cadastro do cliente, forem iguais aos parâmetros **MV****\_CLIPAD e** **MV\_LOJAPAD,** o campo **"Vlr. Acumul** **A1\_VACUM"** não será preenchido (.F.).

**A1\_VACUM** = Valor Acumulado das Vendas no Ano para este cliente. O campo é incrementado ao incluir um título a receber do respectivo cliente (se excluir o título, o campo é atualizado também, subtraindo-se o valor da exclusão).

Os campos **"Moeda LC A1\_MOEDALC"** e **"Moeda** **C5\_MOEDA"** devem conter a mesma informação de moeda para que o campo **"Vlr. Acumul** **A1\_VACUM"** seja atualizado.  
  
Para ajuste dos valores do campo rode a rotina (FINA410).  
Ref Dados Cli/For: Módulo Financeiro > "Miscelânea > Recálculos > Ref Dados Cli/For" - que Refaz o Cálculo de campos como o **"Saldo Título A1\_SALDUP"**.

![cadastro.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016350191)

**Observação**: Nesta rotina há o Parâmetro: "Recalcula Dados Históricos?"  
Este processo atualiza as informações de vendas informadas na tabela **SA1** que não sofrem alterações automáticas nos seguintes campos:  
"Saldo Título A1\_SALDUP", "Sld. Moed. For A1\_SALDUPM", "Saldo LC Sec A1\_SALFIN", "Sld. LC Se MF A1\_SALFINM", "Maior Dupl. A1\_MAIDUPL", "Atrasados A1\_ATR","Pag. Atras. A1\_PAGATR", "Nro Pagtos A1\_NROPAG", "Vlr. Acumul A1\_VACUM", "Maior Saldo A1\_MSALDO", "Media Atraso A1\_METR" e "Maior Atraso A1\_MATR".

Em caso de dúvidas na rotina, contate nossa Equipe de Suporte Financeiro Protheus.

**Saiba Mais:**  
**[FIN0027\_Refaz\_dados\_cliente\_fornecedor](http://tdn.totvs.com/display/PROT/FIN0027_Refaz_dados_cliente_fornecedor)**
