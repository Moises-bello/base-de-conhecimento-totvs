---
article_id: 25744857444631
category: GESTOR
content_hash: 3ceb639fe0fbe70d52bbbb920f35b83c269df60fff4c6fce102e634b88707ee3
fetched_at: '2026-06-28T22:44:35.452668+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - MEU RH - Não mostra funcionário na Minha equipe quando
  MV_ORGCFG=0
type: support-article
updated_at: '2026-06-15T13:17:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25744857444631-RH-Linha-Protheus-MEU-RH-N%C3%A3o-mostra-funcion%C3%A1rio-na-Minha-equipe-quando-MV-ORGCFG-0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25744844479895) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Não mostra funcionário na Minha equipe quando MV\_ORGCFG=0  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Sistema faz uma *query* / validação, como exemplo abaixo, se por ventura, alguma delas falhar, não irá ser retornado dados nessa validação, e consequentemente **não demonstrará o funcionário.**  
  
**QB\_DEPTO = RA\_DEPTO** - Código do departamento na SRA existe na **SQB - Tabela de Departamentos**?  
**RJ\_FUNCAO = RA\_CODFUNC** - Código da função na SRA existe na **SRJ - Tabela de Funções?** (Esse caso é o mais recorrente)  
**QB\_MATRESP = RA\_MAT** - Código da matricula responsável do departamento, existe na **SRA - Tabela de Funcionário?**  
**RD0\_CODIGO = RDZ\_CODRD0 - RD0\_CODIGO** do participante é o mesmo no campo **RDZ\_CODRD0 - Tabela de Vínculos do participantes?**  
RA\_SITFOLH <> 'D' - **Funcionário Esta ativo?**  
  
Existe também a possibilidade do campo QB\_KEYINI, Chave de busca das solicitações estar com conteúdo inválido e precisa ser refeito. [Nessa documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058413613-RH-Linha-Protheus-MEU-RH-O-que-fazer-quando-as-Solicita%C3%A7%C3%B5es-n%C3%A3o-seguem-os-N%C3%ADveis-ou-Fluxo-de-aprova%C3%A7%C3%A3o-desejado) tem os detalhes para refazer o conteúdo do campo.  
  
Cabe ressaltar que, se for uma implantação recente da Hierarquia de Aprovação por Departamentos, utilizar a documentação a seguir como base:  
[**RH - Linha Protheus - MEU RH - Como configurar a hierarquia por departamentos (MV\_ORGCFG=0)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7917580297623)  
  
**Saiba Mais**  
[**Meu RH - O que conferir quando no Meu RH do Gestor, as rotinas relacionadas à Gestão não aparecem**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32765571785367-RH-Linha-Protheus-Meu-RH-O-que-conferir-quando-no-Meu-RH-do-Gestor-as-rotinas-relacionadas-%C3%A0-Gest%C3%A3o-n%C3%A3o-aparecem)  
[**CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
