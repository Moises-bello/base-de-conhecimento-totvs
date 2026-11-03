---
article_id: 360035066073
category: Contabilidade Gerencial - Calendário Contábil
content_hash: 02ea48c9c9342c42769b03c53980e9e0a2f7ccb1b289b1c6da0573af459b2d8c
fetched_at: '2026-06-28T22:41:03.400378+00:00'
product: protheus
section_id: 1500001537301
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA010 - Como funciona
  a funcionalidade - Bloqueio por Processo
type: support-article
updated_at: '2024-12-04T12:10:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035066073-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA010-Como-funciona-a-funcionalidade-Bloqueio-por-Processo
---

**Dúvida**

Qual a funcionalidade do Bloqueio por Processo?

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 11.80  
  
**Solução**O objetivo desta funcionalidade é atender o processo de fechamento contábil, permitindo o usuário bloquear a movimentação de outros módulos, além da contabilidade de forma unificada, garantindo assim a integridade do fechamento contábil.

Processos/módulos disponíveis para bloqueio.

* Ativo Fixo
* Compras
* Contábil
* Estoque
* Financeiro – Contas a Pagar
* Financeiro – Contas a Receber

Fluxograma macro

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044822834)**

**Descrição do Processo**

* O usuário, através do menu Atualizações, Cadastros, seleciona a opção “Calendário Contábil”.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045684993)

* O usuário seleciona o calendário contábil e através do botão Outras Ações, seleciona “Bloqueio de processo”. O sistema mostra tela com os períodos contábeis e os processos que permitem o bloqueio.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045685013)

* O usuário altera o status dos processos para bloqueado e confirma.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044822874)

 O sistema atualiza a tabela de bloqueio.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045685073)

* Caso algum usuário tente realizar o processo no período bloqueado, o sistema não irá permitirá efetivar a contabilização.

**Opções de Status para o bloqueio por processo:**

* **1 -**Aberto: Indica que o período pode receber lançamentos normalmente;
* **2 -**Fechando: Indica que o período já foi encerrado e **nenhum** lançamento pode ser efetuado.
* **3 -**Transportado: Indica que o período já foi encerrado e transportado para uma base backup. **Nenhum** lançamento pode ser efetuado.
* **4 -** Bloqueado: Indica que este período está temporariamente bloqueado para lançamentos contábeis.
* **5 -** Período: Indica que o período informado se encontra bloqueado e **nenhum** lançamento pode ser efetuado.

**Importante:** Para o correto funcionamento e necessário que as tabelas abaixo estejam com o mesmo compartilhamento

**CTE** - Moeda X Calendário  
**CTG** - Calendário Contábil  
**CQD** - Bloqueio do calendário Contábil   
**CTO** - Moeda cadastrada

O parâmetro [MV\_CTBCACH -](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000666227-MP-SIGACTB-Como-funciona-o-cache-no-ambiente-cont%C3%A1bil-?source=search)foi criado para atender a rotina Lançamento Contábeis Automáticos(CTBA102), ele indica se o calendário contábil, moeda, câmbio e as entidades contábeis (Plano de Contas, Centro de Custos, Item Contábil e Classe de Valor) devem utilizar as informações em cachê, a fim de otimizar a performance.

<https://tdn.totvs.com/pages/releaseview.action?pageId=339511532>
