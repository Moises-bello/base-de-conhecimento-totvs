---
article_id: 360058961994
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 12dded1769e9cf6510d99e79935d2d97a0363cbca4b7853a78556653e1a942ef
fetched_at: '2026-06-28T22:39:56.398269+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Configuração
  Totvs Colaboração/Neogrid 2.0
type: support-article
updated_at: '2025-07-14T21:19:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058961994-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Configura%C3%A7%C3%A3o-Totvs-Colabora%C3%A7%C3%A3o-Neogrid-2-0
---

**Dúvida**Configuração da NFSe no Totvs Colaboração/NEOGRID 2.0  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**O TOTVS Colaboração 2.0 usa o Client NeoGrid, que é o responsável pelo tráfego dos arquivos gerados pelo Microsiga Protheus® x Neogrid/Prefeitura.  
Esse serviço deve ser contratado, pois não está disponível na versão padrão do Protheus.  
A instalação do Client NeoGrid é de responsabilidade da Neogrid.

**Rotina de transmissão:**  
FISA022 - NFSe  
Atualização: [Pacote Documentos Eletrônicos](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)  
  
**Rdmake:**  
NFSEXMLUNI - Importante manter o parâmetro **MV\_NFSEMOD=.F.**  
Atualização: [Pacote Rdmakes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061699513-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Atualiza%C3%A7%C3%A3o-rdmake-NFSEXMLENV)  
  
**Parâmetros:**  
**MV\_TCNEW:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099409054)  
**MV\_NGOUT:**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000526902)  
**MV\_NGINN:**  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000536721)  
**MV\_NGLIDOS:**  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000536741)

**SCHEDULE - COLAUTOREAD:**Toda a movimentação dos arquivos entre as pasta é feita pelo schedule.

No **Configurador (SIGACFG),** acesse **Ambiente/ Schedule/ Schedule**.

1. Clique em **Agent/ Cadastro**.
2. Em **Detalhes** clique em **Incluir**.
3. Informe um nome para o agente.
4. No campo **IP** e **Porta** informe os mesmos dados do **Microsiga Protheus®**.
5. Informe o grupo de empresas.
6. No campo **Número de Threads**, informe a opção **4**.
7. Confira dos dados e confirme.  
     
   ![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000541221)
8. Clique em **Agendamentos/Cadastro**.
9. Em **Detalhes** clique em **Incluir**.
10. Informe o nome da rotina **COLAUTOREAD.**
11. Selecione a empresa/ filial desejada e o módulo correspondente.  
      
    ![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000541381)
12. Clique na opção **Recorrência** e marque **Sempre Ativo**.  
      
    ![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000541501)
13. Clique em **Confirmar** para o agendamento.
14. Clique em **Agent** e clique em **Iniciar Todos os Serviços**.  
      
    ![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099414834)

Após criação do schedule, reinicie o serviço.  
Note que no Appserver.ini desse serviço, os jobs abaixo serão criados:  
  
**[OnStart]**  
jobs=FWSCHDMANAG,FWSCHDQUEUE  
RefreshRate=120  
  
**[FWSCHDMANAG]**  
Main=FWSCHDMANAG  
Environment=  
  
**[FWSCHDQUEUE]**  
Main=FWSCHDQUEUE  
Environment=

Para visualizar no console o processamento do Schedule em tempo real, habilite na seção Enviroment do Appserver.ini o parâmetro **COLAUTOREAD\_DEBUG=1.**  
**Tabelas:**  
CKP – Parâmetros TOTVS Colaboração  
CKQ – Monitor de documentos TOTVS Colaboração  
CKOCOL – Controle de arquivos TOTVS Colaboração  
  
Maiores detalhes:  
[P12 - TOTVS COLABORAÇÃO 2.0](https://tdn.totvs.com/pages/releaseview.action?pageId=187534008)
