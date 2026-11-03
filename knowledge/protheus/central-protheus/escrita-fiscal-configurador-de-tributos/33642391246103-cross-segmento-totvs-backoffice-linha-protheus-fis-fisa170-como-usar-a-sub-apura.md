---
article_id: 33642391246103
category: Escrita Fiscal - Configurador de Tributos
content_hash: a90fb6aa15a039fee53b21894ec68c38891cf273681e7c06ce97ad39134ee948
fetched_at: '2026-06-28T22:39:17.505632+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como usar
  a Sub Apuração junto com o configurador de tributos
type: support-article
updated_at: '2025-07-22T19:07:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33642391246103-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-usar-a-Sub-Apura%C3%A7%C3%A3o-junto-com-o-configurador-de-tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33642391220247) Tempo aproximado para leitura: 00**:**03:00 min  
  
**Dúvida**  
Como usar a Sub Apuração junto com o configurador de tributos   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**

Para que a Sub Apuração seja gerada corretamente por meio da rotina FISA170 – Configurador de Tributos, é indispensável que todos os impostos envolvidos na operação estejam previamente configurados na rotina do Configurador de Tributos, juntamente com os respectivos códigos de lançamento que serão utilizados nas apurações fiscais.

#### Requisitos no TES

Atualmente, mesmo utilizando o Configurador de Tributos, é necessário que determinados campos da TES estejam devidamente preenchidos para que a Sub Apuração funcione corretamente. O campo obrigatório é:

* **Nr. Livro (F4\_NRLIVRO)**:  
  Deve ser informado o número do livro fiscal correspondente à operação.  
  **Exemplos**: 1, 2 ou 3.

#### Parâmetro obrigatório

Além da configuração no TES, é **imprescindível** a definição do parâmetro abaixo para habilitar o uso da Sub Apuração:

| Nome da Variável | MV\_APUSEP |
| --- | --- |
| Tipo | 1 - Caracter |
| Conteúdo | <branco> |
| Descrição | Informar o número dos livros que indicam as Apurações Separadas |
| Exemplo | 1/2/3 |

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33642391220887)

#### Referência SPED Fiscal

A configuração deve estar de acordo com as exigências do **SPED Fiscal**.  
Documentação oficial:  
[SPED Fiscal - Protheus (TDN)](https://tdn.totvs.com/display/public/PROT/SPDFIS+-+Sped+Fiscal)

#### Exemplo de operação

* **Pedido de venda**: Operação com crédito presumido em operações internas no estado de SC.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33642391221655)

#### **Apuração**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33642391224727)

#### **Sub Apuração**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33642391226903)

Para mais detalhes sobre configuração e utilização da rotina, consulte:  
[Procedimentos – FISA170 (Central de Atendimento TOTVS)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055360933-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Procedimentos-de-configura%C3%A7%C3%A3o-e-utiliza%C3%A7%C3%A3o-da-rotina-Configurador-de-Tributos)
