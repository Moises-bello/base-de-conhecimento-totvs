---
article_id: 35344118632215
category: Escrita Fiscal - Configurador de Tributos
content_hash: bda0b49870093f13b1c8fbe8a4d5c9dc7df4ec7418613b61cec7e0a6a83a7030
fetched_at: '2026-06-28T22:39:17.522694+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Mecanismo
  de aprovação de Regras de Cálculo (campo Status) no Configurador de Tributos
type: support-article
updated_at: '2025-10-01T22:10:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35344118632215-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Mecanismo-de-aprova%C3%A7%C3%A3o-de-Regras-de-C%C3%A1lculo-campo-Status-no-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35344087781399) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Qual a finalidade do campo Status na Regra de Calculo dentro do Configurador de Tributos?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - A partir da versão 12.1.2310

**Causa**  
Antes dessa funcionalidade, todas as regras tributárias criadas ou alteradas eram consideradas ativas, sem distinção de homologação ou produção.

**Solução**  
Foi incluído o novo campo **F2B\_STATUS** na tabela de regra tributária (F2B).

* Tipo: (tamanho 1)
* Valores possíveis:  
  ‑ “1” = Em Teste  
  ‑ “2” = Aprovada
* O campo é obrigatório e participa do índice da tabela.
* O filtro de consulta padrão ao buscar regras foi alterado para excluir as regras em fase de teste (a menos que se esteja tratando do ambiente de simulação).

**Definição de Status e Regras de mudança:**

* Enquanto estiver como “1 – Em Teste”, a regra não deve impactar operações fiscais reais.
* Somente é permitido alterar o status para “2 – Aprovada” (não é permitida reversão de “Aprovada” para “Em Teste”).
* A autorização de aprovação pode ser feita de duas maneiras:

  a) **Diretamente no cadastro da regra**  
  ‑ Quando o status estiver em “1 – Em Teste”, ao editar o registro, o campo de Status fica disponível para alteração para “2 – Aprovada”.  
  ‑ Ao confirmar a alteração, o sistema executa a aprovação.

  b) **Via tela (browse) da rotina de regras**  
  ‑ Na listagem de regras, selecionar a regra desejada → “Outras Ações” → “Aprovação de Regras”.  
  ‑ O sistema verifica se a regra é passível de aprovação (status = Em Teste).

**Procedimento de utilização:**

1. Acesse o Configurador de Tributos → Cadastro de Regras (rotina FISA160 ou equivalente).
2. Ao criar ou alterar uma regra, deixe o status em **“1 – Em Teste”** (padrão).
3. Realize os testes necessários (ex: no Simulador de Operações) para validar o comportamento da regra.
4. Quando estiver seguro para promoção para produção, vá ao cadastro da regra (ou na listagem) e selecione “Aprovar Regra”.
5. Caso existam regras dependentes, o sistema exigirá a aprovação em cadeia.
6. Após aprovação, o status será “2 – Aprovada” e não poderá mais voltar para “Em Teste”.
7. A regra aprovada passa a ser considerada nas operações fiscais reais.

**Documentações relacionadas:**

[CFGTRIB - Mecanismo de aprovação de regra](https://tdn.totvs.com/pages/releaseview.action?pageId=942068847)
