---
article_id: 30371620978455
category: TAF - eSocial - Eventos Periódicos
content_hash: 04e4d2bf723750ee782d17f261797864b8f6d288ae3ef9a5ef6201d2380b4b71
fetched_at: '2026-06-28T22:45:19.157384+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos de Tabela, Periódicos e Não
  Periódicos - Código da Ocorrência 609: Código Inválido.'
type: support-article
updated_at: '2026-06-25T11:35:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30371620978455-RH-Linha-Protheus-TAF-eSocial-Eventos-de-Tabela-Peri%C3%B3dicos-e-N%C3%A3o-Peri%C3%B3dicos-C%C3%B3digo-da-Ocorr%C3%AAncia-609-C%C3%B3digo-Inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30371620953111) Tempo aproximado para leitura: **00:03:00 min****Ocorrência****Ao tentar transmitir o evento é apresentada a mensagem de rejeição abaixo:  
  
Sequência: 000001 - Tipo: Erro - Código da Ocorrência: 609  
Localização: /eSocial/envioLoteEventos/eventos/evento/@Id  
Descrição: Código Inválido.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30371620953879)****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões.  
  
**Solução**O ID do evento deve seguir conforme a seguinte regra do eSocial:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30371590124439)  
  
Para corrigir o erro:  
  
**1.** Realize a exclusão do evento rejeitado no TAF;  
 **2.** Gere/Integre novamente o evento a partir do seu ERP para o TAF  
  
**3.** Acesse a rotina Complemento Cadastral no TAF:  
**Caminho: SIGATAF (Módulo 84) > Atualizações > Configs. TAF > Complemento Cadastral  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30371620956695)  
  
4.**Valide se o campo **CPF Transmi.** está preenchido no cadastro da Empresa/Filial:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30371620957847)  
  
**5.** Caso o campo informado no **Passo 4** estiver preenchido, limpe o campo e salve o registro.  
**Obs.: O campo de CPF só deve ser preenchido em caso de produtor rural.  
  
6.** Em caso de Outorga, o CNPJ ou CPF são preenchidos no campo **CNPJ Transmi.**mesmo com pontuação incorreta.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30372102531735)  
  
O campo é preenchimento automaticamente ao realizar a configuração do **Certificado Digital** ao inserir os dados de outorga no campo de **CNPJ ou CPF diferente do empregador**:  
**PASSO 10** - [RH - Linha Protheus - TAF - eSocial - Configuração - TSS - Certificado Digital A1 - Como Efetuar Preparação do Certificado Digital e Configurá-lo no TAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034159554-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-TSS-Certificado-Digital-A1-Como-Efetuar-Prepara%C3%A7%C3%A3o-do-Certificado-Digital-e-Configur%C3%A1-lo-no-TAF)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30372154975767)  
  
**7.** Após validações, tente transmitir o evento novamente.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
