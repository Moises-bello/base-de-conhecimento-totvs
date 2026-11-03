---
article_id: 360019168831
category: Financeiro - Consultas / Relatórios
content_hash: 5153e53f82ff802c0235544e41f1cdff10ba817b3013bb4fd80469f30755bfdd
fetched_at: '2026-06-28T22:37:58.403020+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - ERRORLOG type mismatch
  on compare on REPORTPRINT(FINR150.PRX)
type: support-article
updated_at: '2022-04-18T18:19:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019168831-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-ERRORLOG-type-mismatch-on-compare-on-REPORTPRINT-FINR150-PRX
---

**Ocorrência**Ao gerar o relatório de títulos a pagar (**FINR150**), e ocorrer o erro Type mismatch on compare  on REPORTPRINT(**FINR150.PRX**)

Como Exemplo abaixo:

![Erro_fina150.PNG_-_Visualizador_de_Fotos_do_Windows.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360014917311/Erro_fina150.PNG_-_Visualizador_de_Fotos_do_Windows.jpg)  
**Causa**

Esse erro é apresentado quando o Grupo de perguntas do relatório não está atualizado ou alguma pergunta está classificada incorretamente (Tipagem Ex. **Carácter, Númerico** etc.. )

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.17  
  
**Solução**

1. Para Solucionar se faz necessário atualizar o ambiente com o ultimo dicionário de dados e executar o compatibilizador **UPDDISTR**.

**Importante:**Sempre é indicado estar com Dicionario de dados atualizados
