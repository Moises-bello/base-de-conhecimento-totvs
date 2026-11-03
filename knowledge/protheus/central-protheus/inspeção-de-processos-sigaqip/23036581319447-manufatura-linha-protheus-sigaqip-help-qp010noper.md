---
article_id: 23036581319447
category: Inspeção de Processos (SIGAQIP)
content_hash: 92892a60d2c803a9f27fe11099e4969575e8069d52df3e4ee26dbe4ecfd24df4
fetched_at: '2026-06-28T22:42:25.772436+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Help QP010NOPER
type: support-article
updated_at: '2026-02-11T19:45:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23036581319447-Manufatura-Linha-Protheus-SIGAQIP-Help-QP010NOPER
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23036576525719) Tempo aproximado para leitura: **00:00:55 min**  
  
**Ocorrência**  
Na rotina **QIPA010 - Especificação de Produto** ao cadastrar Ensaio, Rastreamentos, Observações, Família de Instrumentou e/ou Não-Conformidades ocorre o *help* **QP010NOPER - Não será possível realizar a associação de: Ensaios, Rastreamentos, Observações, Família de Instrumento e/ou Não-Conformidades à Operação corrente**.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**  
Este *help* **QP010NOPER** é exibido quando campos obrigatórios da especificação de produto não foram preenchidos, quando o parâmetro **MV\_QIPMAT - Indica se o módulo de Insp.de Processos está integrado com materiais tem conteúdo** igual a **N - Não**, ou quando o produto não tem cadastro na rotina **PCPA124  - Processo Produtivo (tabela SG2)** na **filial selecionada**.  
  
  
**Solução**  
Para solucionar a ocorrência, verifique se os campos a seguir estão preenchidos:  
1. Valide se o parâmetro **MV\_QIPMAT - Indica se o módulo de Insp.de Processos está integrado com materiais** tem conteúdo igual a **S - Sim**;  
2. Valide se o produto tem cadastro na rotina **PCPA124  - Processo Produtivo (tabela SG2)** na **filial selecionada;**  
**3.** Valide se os campos da especificação de produto foram preenchidos: 1. **Operação**; 2. **Recurso**; 3. **Descr. Oper.**; 4. **Tempo Padrão**; 5. **Tipo Operac**.; 6. **Oper. Obrig.**; 7. **Seq. Obrig.**; 8. **Laudo Obrig.**.
