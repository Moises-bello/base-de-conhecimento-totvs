---
article_id: 360060052933
category: Recrutamento e Seleção de Pessoas (SIGARSP)
content_hash: 7586a9a18c53927b54780ddd539f967f1c8205fafe5b2a11a8fb4b176797a58b
fetched_at: '2026-06-28T22:43:00.914117+00:00'
product: protheus
section_id: 206960907
source: central-protheus
title: RH - Linha Protheus - RSP - É possível efetuar admissão do Candidato após aprovação
type: support-article
updated_at: '2021-04-06T19:37:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060052933-RH-Linha-Protheus-RSP-%C3%89-poss%C3%ADvel-efetuar-admiss%C3%A3o-do-Candidato-ap%C3%B3s-aprova%C3%A7%C3%A3o
---

**Dúvida**Após aprovação do Candidato, é possível fazer admissão pelo módulo Recrutamento e Seleção Pessoas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Recrutamento e Seleção de Pessoal - Todas as versões  
  
**Solução**Sim, é possível migrar as informações para o Cadastro de Funcionário (SRA), através da rotina Admissão (RSPM001) do módulo SIGARSP.   
  
É necessário configurar o parâmetro **MV\_RSPDEPA**, no módulo Configurador e o arquivo RSDEPA.TXT deve conter os campos DE/PARA que trarão preenchido na rotina da Admissão.   
  
A rotina de Admissão fica no menu Miscelânea > Admissão, que faz uso do arquivo RSDEPA.TXT que segue na sua estrutura os campos do currículo e serão utilizados para migrar informações para a SRA (Funcionários), facilitando o preenchimento de parte dos campos e por sua vez permite fazer manutenção inserindo mais campos caso necessite.  
  
Já o arquivo RSDEPA2.TXT é utilizado quando se faz uso da rotina de Seleção Interna (RSPM002.PRW), que irá buscar os dados do cadastro de funcionários para o cadastro de currículos, processo inverso.  
  
Segue link que contém mais informações sobre o [Arquivo RSPDEPA.TXT](https://tdn.totvs.com/pages/releaseview.action?pageId=233738084)  
  
**Saiba Mais****[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048093-RH-Portal-do-Candidato)**[para acessar artigos e informações sobre Portal do Candidato](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048093-RH-Portal-do-Candidato)
