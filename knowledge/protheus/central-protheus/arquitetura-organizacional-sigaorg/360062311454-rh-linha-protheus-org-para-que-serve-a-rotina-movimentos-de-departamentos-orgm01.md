---
article_id: 360062311454
category: Arquitetura Organizacional (SIGAORG)
content_hash: cf36973963d69ad4a4bf9db31e6929d66f3313930837cbf2ba1f9b37089190b4
fetched_at: '2026-06-28T22:42:52.916096+00:00'
product: protheus
section_id: 1500000904101
source: central-protheus
title: RH - Linha Protheus - ORG - Para que serve a rotina Movimentos de Departamentos
  (ORGM010) e como incluir
type: support-article
updated_at: '2025-02-21T17:20:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062311454-RH-Linha-Protheus-ORG-Para-que-serve-a-rotina-Movimentos-de-Departamentos-ORGM010-e-como-incluir
---

**Dúvida**Para que serve a rotina Movimentos de Departamentos (ORGM010) e como incluir?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Arquitetura Organizacional - Todas as versões  
  
**Solução**O objetivo desta rotina é realizar e registrar todas as solicitações, aprovações e cancelamentos dos postos para os departamentos, mantendo um histórico com suas respectivas datas, solicitantes e aprovadores.  
Assim as movimentações efetuadas ficam registradas, mantendo o histórico desde a solicitação até o cancelamento, armazenando também a informação da data e de quem efetuou a movimentação.  
Acesse  o Módulo 70 (**SIGAORG**), no caminho: **Atualizações > Movimento > Departamento > Incluir**  
Preencha os dados conforme orientações de help de campo.  
  
Observe, porém, o seguinte campo: **Tp. Posto**: define se o tipo de posto criado no departamento é individual ou genérico.  
  
• Se selecionada a opção **individual**, o número informado no campo "Qtde. Solicitada" indica a quantidade de postos existentes a ser ocupado, ou seja, 1 posto para um ocupante.

• Quando selecionada a opção **genérica** a quantidade do campo "Qtde. Solicitada" indica o número de postos criados, independente do número de ocupantes, assim, se informado 1, este posto pode ter qualquer número de ocupantes.

Confira os dados e confirme.  
  
![5LKBl0WcSX.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004016782)  
  
A integração entre os postos criados no módulo Arquitetura Organizacional com as vagas do módulo Recrutamento e Seleção, se dá pela configuração do parâmetro **MV\_IORGRSP**. Maiores informações consulte: [MP - RSP - Como Habilitar a integração entre o módulo Recrutamento e Seleção de pessoal com Arquitetura Organizacional](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036460814-MP-RSP-Como-Habilitar-a-integra%C3%A7%C3%A3o-entre-o-m%C3%B3dulo-Recrutamento-e-Sele%C3%A7%C3%A3o-de-pessoal-com-Arquitetura-Organizacional)  
  
**Saiba Mais**  
[Artigos sobre Arquitetura Organizacional](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206968028-RH-Arquitetura-Organizacional)  
[Artigos sobre Portal Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
