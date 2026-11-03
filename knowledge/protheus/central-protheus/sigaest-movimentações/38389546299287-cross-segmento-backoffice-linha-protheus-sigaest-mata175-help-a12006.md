---
article_id: 38389546299287
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f061c31c3798f90f0dc38c0e2b1f320249fae983fa0b66da75097ea69a24912a
fetched_at: '2026-06-28T22:38:55.793393+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA175 HELP A12006
type: support-article
updated_at: '2026-02-16T14:42:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38389546299287-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA175-HELP-A12006
---

O erro HELP A12006 no Protheus ocorre durante a liberação ou rejeição de Controle de Qualidade (CQ) quando campos obrigatórios não são preenchidos. É necessário conferir todos os campos essenciais e customizados, além de testar sem customizações para identificar a causa antes de acionar o suporte.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38389546285975) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao efetuar uma liberacao ou rejeicao de CQ ocorre o HELP A12006  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Durante o processo de **Liberação de CQ (Controle de Qualidade)**, ao tentar concluir a operação, o sistema interrompe o processamento e apresenta o **HELP A12006**.

**Mensagem de Erro:**

> *"Problema: Existem alguns campos obrigatórios no item que não foram informados."*

### **Causa Raiz**

Este é um comportamento padrão do Protheus que atua como uma trava de integridade. O erro indica que o dicionário de dados identificou a ausência de informações em campos marcados como **obrigatórios** para a conclusão do movimento, nas tabelas envolvidas do processo de baixa.

#### 

## **Conferência de Dados Básicos**

Verifique se as informações essenciais na linha do item (grid) foram devidamente preenchidas, com foco nos seguintes campos:

* **Código do Produto**
* **Quantidade**
* **Preço Unitário**
* **Data Prevista**
* **Armazém (Local)**

#### 

## **Campos Customizados e Dicionário**

Caso os campos acima estejam preenchidos, o problema pode estar em campos específicos do seu ambiente:

1. Verifique se foram criados **campos de usuário** (campos iniciados com `_`) nas tabelas relacionadas ao processo de inspeção e se algum deles foi marcado como obrigatório, mas não está sendo alimentado.
2. Confirme se algum campo padrão teve sua obrigatoriedade alterada indevidamente no **Configurador (SIGACFG)**.

Se todos os campos visíveis estiverem preenchidos e o erro persistir, siga os passos abaixo antes de acionar o suporte:

1. **Teste sem Customizações:** Execute o processo com o parâmetro `IXBLOG=NORUN` ou desabilite **Pontos de Entrada** e **Gatilhos** para isolar se a falha é causada por uma regra de negócio específica da empresa.
2. **Pilha de Chamadas (Call Stack):** Caso o erro ocorra, pressione as teclas `SHIFT + F6` (quando aparecer a mensagem de HELP) para capturar a "pilha de chamadas" no momento do Help.
3. **Evidência para o Suporte:** Se for necessário abrir um ticket, anexe:

   * Print da tela com todos os campos preenchidos.
   * Print da pilha de chamadas (*Call Stack*).
   * ID da Central de Diagnóstico atualizado.

Saiba Mais:

[Clique aqui e veja mais artigos sobre Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
