---
article_id: 21251906308119
category: TAF - eSocial - Eventos Periódicos
content_hash: 3bbfc1133370827450287d04dc1b98ffadbcc28f7f9d2d66fabdb3a66f02fe8b
fetched_at: '2026-06-28T22:45:18.988977+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1200 - Código
  da Ocorrência: 553 - Grupo ‘Informações complementares contratuais do trabalhador’
  não deve ser preenchido. Verifique as condições de preenchimento no leiaute.'
type: support-article
updated_at: '2026-06-24T21:37:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21251906308119-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1200-C%C3%B3digo-da-Ocorr%C3%AAncia-553-Grupo-Informa%C3%A7%C3%B5es-complementares-contratuais-do-trabalhador-n%C3%A3o-deve-ser-preenchido-Verifique-as-condi%C3%A7%C3%B5es-de-preenchimento-no-leiaute
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21251953033495) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Ao tentar transmitir um evento S-1200 ( Remuneração de Trabalhador), de um colaborador que possui S-2300 (Trabalhador sem Vínculo de Emprego), o governo eSocial retorna a inconsistência abaixo:  
  
***Sequencia: 000001 – Tipo: Erro – Codigo da ocorrência: 553***  
***Localização: /eSocial/evtRemun/dmDev***  
***Descrição: Grupo ‘Informações complementares contratuais do trabalhador’ não deve ser preenchido. Verifique as condições de preenchimento no leiaute.***

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TAF - eSocial - Todas as versões  
  
**Causa**  
No XML do TAF. a informação de **CBO** é carregada indevidamente para colaboradores que possuem o evento S-2300.  
  
**Solução**  
Para corrigir o erro, peço verificar os pontos listados abaixo:

**1.** O ambiente precisa estar atualizado com a última **Expedição Contínua do TAF**, links para download abaixo:  
12.1.2210 - Para segregados e para clientes Protheus que possuem Garantia Estendida:  
<https://suporte.totvs.com/portal/p/10098/download?e=1084563>

12.1.2310:  
<https://suporte.totvs.com/portal/p/10098/download?e=1126399>

12.1.2410:

<https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1174332>

12.1.2510:

<https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1228187>

**Para mais detalhes referente a atualização do TAF, verifique a documentação abaixo:**  
[Automação Fiscal - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239)  
  
**2**. Se o ambiente estiver atualizado, abra a rotina do **Monitor** (Painel eSocial) e verifique se existe evento **S-2300** para o CPF pendente de transmissão. Caso possua, analise o registro, exclua ou transmita o evento ao governo (eSocial) para que o registro fique de acordo no TAF.   
  
**3**. Acesse o Histórico de Alterações do Funcionário no TAF (Atualizações > Eventos eSocial > Trabalhador > Cadastro Trabalhador > Outras Ações > Exibir Histórico de Alterações) e verifique se o campo **Status de Transmissão** está como **Transmitido Válido** e o campo **Ativo** como **Ativo**. Também verifique se ao visualizar o registro, aba **Info. Controle eSocial**, o campo Nº Recibo está preenchido corretamente.  
  
**4.** Se as informações de cadastros no TAF estiver corretas, conforme descrição acima e o ambiente estiver atualizado, entre em contato com o ERP (Protheus Recursos Humanos, RM Labore, Datasul, etc.) para validação do XML que está sendo encaminhado para o TAF.  
  
**5.** Após manutenções, exclua o evento S-1200 inconsistente no TAF, integre novamente e tente transmitir.  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "****Eventos****"*  
  
Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
