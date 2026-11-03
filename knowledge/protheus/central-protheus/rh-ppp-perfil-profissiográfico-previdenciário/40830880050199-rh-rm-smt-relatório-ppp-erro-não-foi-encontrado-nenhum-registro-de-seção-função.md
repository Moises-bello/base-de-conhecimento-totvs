---
article_id: 40830880050199
category: RH - PPP ( Perfil Profissiográfico Previdenciário)
content_hash: be8900f08feaff1b6ba7d6cdd7b0f6a84c29987edbc451200b960af48e09ba2c
fetched_at: '2026-06-28T22:43:25.115125+00:00'
product: protheus
section_id: 360011909673
source: central-protheus
title: 'RH - RM - SMT - Relatório PPP Erro: Não foi encontrado nenhum registro de
  seção, função ou alocação externa'
type: support-article
updated_at: '2026-06-02T11:38:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40830880050199-RH-RM-SMT-Relat%C3%B3rio-PPP-Erro-N%C3%A3o-foi-encontrado-nenhum-registro-de-se%C3%A7%C3%A3o-fun%C3%A7%C3%A3o-ou-aloca%C3%A7%C3%A3o-externa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40830880028055) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao gerar o relatório PPP foi apresentada a seguinte mensagem de erro:  
  
ERRO NA GERAÇÃO DO RELATÓRIO: Verifique se os históricos do funcionário estão corretos  
Não foi encontrado nenhum registro de seção, função ou alocação externa  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - **Todas as versões.**  
  
**Solução**  
O erro em questão é apresentado quando o Funcionário foi admitido ou transferido com data superior a **31/12/2022**. O PPP no RM pode ser gerado somente para Funcionário cuja data de transferência e/ou admissão ocorreu até dezembro de 2022.  
  
Para validar as informações realize o seguinte passo:   
  
Acesse o cadastro do **Funcionário | Registros** e valide se a Data de Admissão é posterior à **31/12/2022** ou se ocorreu transferência após a data mencionada.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40831492639511)  
  
**Importante:** Com a entrada do PPP eletrônico o sistema passa a não gerar PPP físicos de Funcionários transferidos ou admitidos após 31/12/2022. Para estes casos deverá utilizar o PPP Eletrônico, baseado nos dados do evento S-2240 enviados ao eSocial através da plataforma [Meu INSS](http://gov.br/meuinss).  
  
**Saiba mais**  
[Emitir PPP Eletrônico - Perfil Profissiográfico Previdenciário](https://www.gov.br/pt-br/servicos/emitir-ppp-eletronico-perfil-profissiografico-previdenciario)
