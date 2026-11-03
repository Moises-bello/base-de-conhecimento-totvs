---
article_id: 360018492691
category: Faturamento - Cenários de Venda
content_hash: 1e3e228b573a02d4ed1d9d62284008ac60a7d7786badf1adeb6121ee8b49a606
fetched_at: '2026-06-28T22:38:34.039861+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: 'Cross Segmentos - BackOffice Protheus - SIGAFAT - Mile: Configuração e Limitações
  na Importação de Tabelas de Preço'
type: support-article
updated_at: '2026-01-15T11:32:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018492691-Cross-Segmentos-BackOffice-Protheus-SIGAFAT-Mile-Configura%C3%A7%C3%A3o-e-Limita%C3%A7%C3%B5es-na-Importa%C3%A7%C3%A3o-de-Tabelas-de-Pre%C3%A7o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31122829607959)*** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**É possível importar apenas um item para uma Tabela de Preços já existente sem impactar os demais registros?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus)  - Faturamento -  a partir da versão 12.  
  
**Solução**

A integração Mile para a Tabela de Preços segue o mesmo princípio das integrações ExecAuto. Isso significa que, ao realizar qualquer alteração nos produtos de uma tabela de preços, o arquivo TXT da integração Mile deve sempre conter todos os registros da grid de produtos dessa tabela. Caso contrário, o sistema irá sobrescrever os produtos não informados, removendo-os da tabela de preços.

Com relação aos demais produtos que não sofrerão alterações, estes deverão conter as mesmas informações gravados na base de dados.

### Como Funciona na Prática?

Se uma tabela de preços já existente contém produtos cadastrados e for necessário alterar ou incluir um novo item, é fundamental que o arquivo TXT inclua:

1. Todos os produtos que já existem na tabela, mesmo que não sofram alterações.
2. Os produtos novos ou alterados, com os respectivos ajustes nos valores.

### Exemplo

Imagine que temos uma Tabela de Preços "ABC", que atualmente contém os seguintes produtos:

* **Produto X** (Sequência 0001) – Preço de venda: R$ 10,00
* **Produto Y** (Sequência 0002) – Preço de venda: R$ 20,00

Agora, queremos alterar apenas o preço de venda do Produto Y para R$ 30,00.

Arquivo TXT funcional:

`|A|ABC|TABELA ABC| -> Código e descrição da tabela de preço`

`|B|0001|10.00| -> Produto X (mantendo o preço original)`

`|B|0002|30.00| -> Produto Y (alterando o preço)`

Observação: O arquivo TXT acima é uma sugestão de configuração podendo ser editada conforme objetivo do usuário. O suporte padrão não valida a Mile em ambientes devido a possíveis particularidades e personalizações.

**Saiba mais:**[Procedimento para Importação e Exportação de Layouts](https://tdn.totvs.com/pages/releaseview.action?pageId=423932458)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Uso da Integração Mile no Modulo Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043730774-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Uso-da-Integra%C3%A7%C3%A3o-Mile-no-Modulo-Faturamento)
