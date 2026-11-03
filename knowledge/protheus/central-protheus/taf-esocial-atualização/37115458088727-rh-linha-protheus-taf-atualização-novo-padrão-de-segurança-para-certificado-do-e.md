---
article_id: 37115458088727
category: TAF - eSocial - Atualização
content_hash: 6a50fbf77bf72f6a697836ab9b3b9f5206d7074c724c8143e89a3e8e272b5176
fetched_at: '2026-06-28T22:45:13.270236+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF - ATUALIZAÇÃO - Novo Padrão de Segurança para Certificado
  do eSocial
type: support-article
updated_at: '2026-06-26T11:43:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37115458088727-RH-Linha-Protheus-TAF-ATUALIZA%C3%87%C3%83O-Novo-Padr%C3%A3o-de-Seguran%C3%A7a-para-Certificado-do-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37115427664279) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
O que devo fazer para atualizar o Certificado do eSocial com o novo Padrão de Segurança?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação Fiscal - e-Social - Atualização - Á partir da versão 12.1.2310

**Solução**

 1. Conforme informado no material do eSocial, o novo Padrão de Segurança só entrará em produção a partir de **JUNHO DE 2026**

[**LNK OFICIAL DO ESOCIAL - Atualização de Certificado do eSocial para um novo Padrão de Segurança**](https://www.gov.br/esocial/pt-br/noticias/atualizacao-de-certificado-do-esocial-para-um-novo-padrao-de-seguranca)  
  
2. Para se adequar ao novo padrão de segurança na data mencionada deverá seguir os passos do material do eSocial:

* O mesmo informa para baixar, instalar/importar duas novas cadeias certificadoras diretamente no Servidor onde são realizadas as transmissões dos eventos Esocial;
* Nesse caso deve ser importadas as novas cadeias certificadoras dentro do servidor onde é EXECUTADO O SERVIÇO DO TSS.
* Ao término do procedimento, observe que as duas novas cadeias certificadoras serão exibidas. Acesse:  
    
  *Painel de Controle do servidor windows > opção Rede e Internet> Opções de Internet > aba Conteúdo > opção Certificados >aba Autoridades de Certificação Intermediárias*  
    
  Exemplo:  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/41434269004567)

 3. CLIENTES CLOUD TOTVS: Não é necessário nenhuma ação, a atualização será realizada automaticamente pelo CLOUD.

🚨**IMPORTANTE🚨**

* Essa atualização NÃO É REALIZADA no sistema TAF ou TSS -  deve ser realizada apenas no servidor onde é executado o serviço do TSS.

**SAIBA MAIS**

Para saber mais consulte os links abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

[Centralizadora TAF](https://tdn.totvs.com/display/public/TAF/Centralizadora+TAF)

[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos"

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
