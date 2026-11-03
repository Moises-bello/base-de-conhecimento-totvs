---
content_hash: 7034943e8ee4c9f7664fa420e6fc5f69f01ad491db418d28010a5241b51e8381
fetched_at: '2026-06-29T00:10:18.454365+00:00'
page_id: '4811926'
product: rm
source: tdn-rm
title: Automatização da Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4811926
version: 4
---

BLOCK

Automatização da Contabilização

FAQ: **Automatização da Contabilização**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.0 |

Solução

**Introdução***A automatização da contabilização garante segurança e uma enorme agilidade aos processos da gestão Financeira minimizando falhas operacionais e custos de operação.*

*Esse recurso fantástico do sistema é disponibilizado através da associação de eventos contábeis à Tabela Opcional ou a Tipo de documentos.*

**Desenvolvimento/Procedimento**

**1.** Definir a Tabela que será utilizada como *Tabela Default para Evento* através do Assistente de implantação de processos / 02.05.01 – Contabilização > Etapa 1 – Contab. Financeiro > Nome do campo: ‘Tabela Default para Evento’.

**2.** Acessar o menu Cadastros e clicar na opção definida conforme o item 1.  
Editar os itens desta tabela e definir o(s) Evento(s) Contábil(eis) a ser(em) utilizado(s), de acordo com cada processo.

**Exemplo de associação:**

Tabela default para evento = Tipo de Documento.

Acessar o menu Cadastros/Tipos de Documento, editar,  serão apresentados na aba “Dados Adicionais” os campos para a indicação dos eventos conforme cada processo. As opções disponíveis são: Evento Contábil, Evento Contábil para Baixa, Evento Contábil para Baixa Contábil, Baixa por Acordo e Baixa de gerados por Acordo.   
Feito isso, ao executar quaisquer desses processos, utilizando esse tipo de documento   a contabilização será feita automaticamente, com a versatilidade de poder alterar o evento durante o processo..

**DICAS:**

1.      Se a Tabela Default para Evento definida for o cadastro de Tipos de Documento, não será possível definir um Evento Contábil default para o Extrato de Caixa, já que não existe campo referente ao Tipo de Documento no Extrato. No caso da Tabela Default ser uma Tabela Opcional, será apresentado além das opções citadas acima, o campo Evento Contábil para o Extrato.

2.      As definições contábeis poderão variar de Tipo de Documento para Tipo de Documento, de acordo com a necessidade de cada operação e com o processo que estiver sendo realizado (inclusão de Lançamento, Baixa, geração de Acordo, etc.).
