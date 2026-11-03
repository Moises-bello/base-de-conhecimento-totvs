---
article_id: 24346599286295
category: TAF - eSocial - Cadastros de empresas
content_hash: a7f35108ae2ab348e7d0d414c7617578d0a1057395683e0965aac1857e48aac9
fetched_at: '2026-06-28T22:45:16.457746+00:00'
product: protheus
section_id: 1500001547962
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos de Tabela - S-1000 -  Código
  da Ocorrência 553: Grupo ''Organismos internacionais e outras instituições extraterritoriais''
  não deve ser preenchido'
type: support-article
updated_at: '2026-06-23T20:51:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24346599286295-RH-Linha-Protheus-TAF-eSocial-Eventos-de-Tabela-S-1000-C%C3%B3digo-da-Ocorr%C3%AAncia-553-Grupo-Organismos-internacionais-e-outras-institui%C3%A7%C3%B5es-extraterritoriais-n%C3%A3o-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26815727254167) Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**No módulo do TAF, ao tentar realizar a transmissão do evento S-1000 (Informações do Empregador/Contribuinte/Órgão Público) é apresentada a seguinte rejeição:  
  
**Sequência: 000001 - Tipo: Erro - Código da ocorrência: 553**   
**Localização: / eSocial/evtinfoEmpregador/infoEmpregador/inclusao/infoCadastro**   
**Descrição: Grupo 'Organismos internacionais e outras instituições extraterritoriais' não deve ser preenchido. Verifique as condições de preenchimento no leiaute.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões. **Causa**   
Essa inconsistência ocorre, pois o campo **Isen. Multa** no **S-1000** está preenchido indevidamente, logo, o grupo **Organismos internacionais e outras instituições extraterritoriais** também está sendo preenchido indevidamente.  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Acesse a rotina de **Complemento Cadastral** no TAF.   
Caminho: Atualizações > Configs. TAF > Complemento Cadastral:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26815733976983)  
Para mais detalhes, verifique a documentação abaixo:  
[Automação Fiscal - Configurações - Como acessar o complemento cadastral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034688453-Automa%C3%A7%C3%A3o-Fiscal-Configura%C3%A7%C3%B5es-Como-acessar-o-complemento-cadastral?source=search)  
  
**2.** Após acessar a rotina, localize o registro em questão, entre como **Alterar** e ajuste o campo **Isen. Multa** do evento conforme a realidade da sua Empresa e a regra do eSocial:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26815727261591)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26815727264279)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26815733987607)  
<https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/index.html#1000_infoEmpregador_inclusao_infoCadastro_infoOrgInternacional>  
  
**3.** Confirme as alterações e tente transmitir o evento novamente.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [**TOTVS Informa**](https://informa.totvs.com/)selecione em categorias a área e pesquise por "**Eventos**"  
  
Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
