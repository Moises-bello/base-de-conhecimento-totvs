---
article_id: 7175886080919
category: GPE - eSocial - Não Periódicos
content_hash: 0422d9c5d2dacee6af10394ae23fa8a723af5ef4ba274bf4f8d797599dcdeacc
fetched_at: '2026-06-28T22:45:04.599938+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200/S-2206 - Como enviar a tag codTreiCap(Informações
  de treinamento) para o eSocial
type: support-article
updated_at: '2026-06-16T11:52:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7175886080919-RH-Linha-Protheus-GPE-eSocial-S-2200-S-2206-Como-enviar-a-tag-codTreiCap-Informa%C3%A7%C3%B5es-de-treinamento-para-o-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25788992635031)**Tempo aproximado para leitura**: 00:01:00 min**

**Dúvida**Como enviar a *tag* codtreiCap (Informações de treinamento) para o eSocial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Acesse no módulo 26 SIGATRM o menu **>Atualizações >Calendário >Treinamentos** e realize o cadastro do treinamento  
  
![xFd5zXE48P.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/7174932337559)  
  
2. No cadastro, realize o **preenchimento do campo Cód.eSocial** (RA2\_ESOC), este campo é o que será enviado a *tag*codtreiCap no S-2200 e S-2206.  
  
Lembrando que o conteúdo desse campo, deve ser valido **de acordo com a tabela 28** do leiaute S-1.0 do eSocial.  
![JAQYS3U9N8.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/7175065534359)  
  
Sistema faz a busca padrão na **tabela S139** na rotina de Manutenções com os Tipos de Treinamento  específico na tabela 28 do eSocial.  
  
**Para *download* da documentação como MOS (Manual de orientação do eSocial) e leiautes, acesse:**  
<https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica>  
  
3. Após cadastrar o Treinamento (TRMA050), é necessário realizar a reserva de Treinamento, para isto acesse o caminho: Atualizações > Calendário > Reservas. Selecione o treinamento (TRMA060), clique em reservar, preencha os parâmetros e confirme.  
  
4. Na geração dos eventos S-2200 ou S-2206 pelas rotinas de cadastro do funcionário, a *tag* codTreiCap será gerada somente dos treinamentos já devidamente finalizados (tabela RA4).  
Para realizar a baixa de um treinamento siga as instruções descritas na documentação abaixo:

[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050782713-RH-Linha-Protheus-TRM-Geração-de-um-calendário-para-treinamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050782713-RH-Linha-Protheus-TRM-Gera%C3%A7%C3%A3o-de-um-calend%C3%A1rio-para-treinamento)  
  
5. **Integração** dos eventos a partir da rotina de Baixa de Treinamentos (TRMA070):

**Atualizações >Calendários >Baixa de Treinamentos**

![OOVjzZBDRD.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/7175432005527)  
  
Documentação completa: <https://tdn.totvs.com/pages/releaseview.action?pageId=647461514>  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus?source=search)
