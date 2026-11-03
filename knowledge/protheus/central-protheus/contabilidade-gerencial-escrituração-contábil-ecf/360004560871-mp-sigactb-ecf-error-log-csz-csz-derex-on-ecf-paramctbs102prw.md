---
article_id: 360004560871
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: da9c6615855037dc32f00f8f553873b06f28f10f51f93f6560bfe9a9822759af
fetched_at: '2026-06-28T22:40:47.568706+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: MP - SIGACTB - ECF - ERROR LOG CSZ->CSZ_DEREX on ECF_PARAM(CTBS102.PRW)
type: support-article
updated_at: '2021-04-28T22:09:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004560871-MP-SIGACTB-ECF-ERROR-LOG-CSZ-CSZ-DEREX-on-ECF-PARAM-CTBS102-PRW
---

**Ocorrência**

Ao entrar no ambiente de contabilidade gerencial/central de escrituração é exibido a mensagem:

THREAD ERROR ([xxxxxxxxxxxxxxxxx]) 04/06/2018 22:09:22  
**invalid field name in Alias CSZ->CSZ\_DEREX on ECF\_PARAM(CTBS102.PRW) 15/05/2018 13:35:18 line : 1250**

**Ambiente**  
Protheus – Contabilidade Gerencial – 12.1.17   
  
**Causa**Esse incidente ocorre, pois após a aplicação do pacote, o sistema está tentando localizar um campo de dicionario que não existe no ambiente.

Este campo foi liberado no dicionário da ECF de 2018  
  
**Solução**

**Passo 1** - [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/706376) para Baixar o dicionário

**Passo 2** - Copiar os arquivo SDFBRA.TXT para a pasta Systemload (Se existir o arquivo na pasta, proceder com a exclusão do arquivo existente e copia do arquivo novo)

Importante

Você deve baixar tanto o arquivo de dicionário completo (SXSBRA.TXT, por exemplo) quanto o dicionário diferencial (SDFBRA.TXT, por exemplo), e descompactá-los na pasta Systemload. Embora a atualização de release utilize apenas o arquivo diferencial, o arquivo completo também deve ser baixado para a pasta, pois futuramente, quando for criar uma nova empresa ou filial, por exemplo, o arquivo que será utilizado será o COMPLETO.

Maiores informações para download dos arquivos no link: [Atualizar o Dicionário de Dados do Protheus 12](http://tdn.totvs.com/pages/viewpage.action?pageId=271415266)

**Passo 3** - Excluir os arquivos de log abaixo:

Dentro da pasta system:

* mpupdlog.log
* mpupdlog.fpt
* mpwizard.hlp
* mpwizardhlp.lck

Dentro da pasta Appserver:

* mpupddistri.tsk

**Passo 5** - Realizar a execução do UPDDISTR em seu ambiente: Atualizador de dicionário e base de dados - UPDDISTR

**Passo 6** - Posteriormente realize a  [Atualização do ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004873211) e o Dicionario do [Pacote de Atualização / Correção - ECF 2018 - Exercício 2019](http://tdn.totvs.com/pages/releaseview.action?pageId=485425635)  
  
 Para maiores informações, acessar o link: <http://tdn.totvs.com/display/public/PROT/ECF0003_Help_wizard_rotina_central_escrituracao_ECF>

Página Centralizadora: <http://tdn.totvs.com/display/PROT/ECF>
