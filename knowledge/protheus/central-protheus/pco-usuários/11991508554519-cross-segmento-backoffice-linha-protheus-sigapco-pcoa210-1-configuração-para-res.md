---
article_id: 11991508554519
category: PCO - Usuários
content_hash: f33907709a39e153334decac4e7cd4627dab6e095e21e7fd69f44b27c40d4b37
fetched_at: '2026-06-28T22:37:08.220044+00:00'
product: protheus
section_id: 1500001539861
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA210_1 - Configuração
  para restrição de acesso de usuários a determinadas configurações de cubos em consultas
  e relatórios.
type: support-article
updated_at: '2023-11-21T14:47:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11991508554519-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA210-1-Configura%C3%A7%C3%A3o-para-restri%C3%A7%C3%A3o-de-acesso-de-usu%C3%A1rios-a-determinadas-configura%C3%A7%C3%B5es-de-cubos-em-consultas-e-relat%C3%B3rios
---

**Dúvida**Como configurar a restrição de usuários a determinadas configurações de cubo, em relação a consulta e relatórios.

**Ambiente**Cross Segmento - Backoffice Linha Protheus -Planejamento e Controle Orçamentário.

#### **Solução:**

O parametro MV\_PCO\_AL3 devera estar configurado como 1 para acesso a rotina.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11990656415255)

Após configuração do parametro, será necessário criar a restrição através da rotina PCOA210\_1

**Exemplo de restrição ao Cubo:**

| Campo | Explicação |
| --- | --- |

| Ativo | Se o controle está ativo ou não. |
| Campo Ent | Campo informativo indicando o campo de referencia da tabela base. |
| Const. Padrão | Consulta padrão desejada a se utilizar. |
| Entidade | Entidade (tabela do sistema) que sofrera restrição de acesso por usuário na faixa informada. |
| Nome Entid | Descrição da entidade gatilhada a partir do campo **ENTIDADE**. |
| Plano | Plano informado. |
| Tamanho | Tamanho do campo que sofrera restrição de acesso. |

**Grid:**

| Campo | Explicação |
| --- | --- |

| Item | Numeração automática. |
| Cod. Usuario | Código do usuário a ser utilizado no controle. |
| Nome | Nome gatilhado do código do usuário. |
| Fx. Inicio | Faixa inicial da entidade que será restrita. |
| Fx. Final | Faixa final da entidade que será restrita. |
| Direito | Operação que o usuário terá acesso ( Visualizar, Alterar, Controle total ). |
| Campo Entd | Campo da entidade escolhida.. |

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11991427133847)

Para que a restrição seja efetivamente controlada no cadastro da "Entidade x Usuário" o campo "Ativo" deve estar ativado (opção "Ativo").

Os campos os campos "Faixa Inicio" e "Faixa Final" permitem definir o intervalo de registros que serão afetados pela restrição. Para preenchimento pode utilizar-se a consulta padrão da entidade acessada pelo botão Pesquisa.

Ao confirmar a consulta ou a emissão do relatório, a tela de parametrização do cubo que se processará, será preenchida com os valores definidos na configuração e o usuário não poderá alterá-los (quando se trate de direito de visualização padrão).

**Saiba mais:**

[Configuração de cubos (PCOA210\_1 - SIGAPCO)](https://tdn.totvs.com/pages/releaseview.action?pageId=312175452)

[Planilhas (PCOA110 - SIGAPCO)](https://tdn.totvs.com/pages/releaseview.action?pageId=312175337)

[Exclusão do acesso à visão gerencial (PCOA210\_4 - SIGAPCO)](https://tdn.totvs.com/pages/releaseview.action?pageId=312175409)
