---
article_id: 1500009382821
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 19163a51a50e04da46719d710598a2dc3ee8657edc271e84cf6324e152362452
fetched_at: '2026-06-28T22:39:09.667259+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Novo Gestor de Stored
  Procedures CFGX051M
type: support-article
updated_at: '2025-03-12T12:17:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009382821-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Novo-Gestor-de-Stored-Procedures-CFGX051M
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28151606921239) Tempo aproximado para leitura: 00:05:00 min**

**Dúvida**

Como instalar as procedures antigas, e novas procedures com a nova gestão de procedures?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todos os Módulos - Todas as versões  
  
**Solução**

Neste artigo documentaremos, em passos, como instalar o Novo Gestor de Procedures que pode ser utilizado a partir da versão 12.1.27 do Protheus.

Acesse também: [Stored Procedures utilizadas no produto Estoque e Custos](https://tdn.totvs.com/x/wi3AFQ)

**Novo Gestor de Stored Procedures – CFGX051M**

O programa **Gerenciador de procedures** **(CFGX051)**, do módulo **Configurador** **(SIGACFG)** passou por uma mudança significativa, além da interface totalmente remodelada, não mais existirem os arquivos de pacotes com extensão **SPS**. Estes arquivos foram substituídos por arquivos de extensão **ZSPS**, que estarão embarcados no **RPO**. Para mais informações acesse [Stored Procedures - Novo gerenciador de pacotes](https://tdn.totvs.com/x/FqDXJg).

Outra grande mudança é a **integração** com a [Central de Atualizações - Protheus](https://tdn.totvs.com/x/OpamHw) para obtenção dos pacotes de procedures mais recentes homologados. Esta integração ocorrerá de maneira transparente visando facilitar o processo de atualização das procedures no ambiente.

***IMPORTANTE:***

***Esta alteração não afeta:***

* *Como as procedures são executadas;*
* *Como são instaladas no banco;*
* *Conteúdo das procedures e dos pontos de entradas;*  
  *Esta alteração apenas muda a interface e a forma como as procedures são distribuídas.*

Vídeo modelo de configuração e instalação das novas procedures:

**Migração para o novo modelo**

Para preparar o ambiente e realizar a migração, tenha certeza de executar os seguintes passos:

**Passo 1:** 

Aplique o patch da Central de Atualizações Release 1.4.1 (ou superior). Para isso acesse a página da [Central de Atualizações - Release Notes](https://tdn.totvs.com/x/n56-Hw) e baixe o patch mais recente disponibilizado.

![](https://tdn.totvs.com/download/attachments/651665430/image2022-4-25_9-32-1.png?version=1&modificationDate=1650889922140&api=v2)

***IMPORTANTE:*** *Mesmo que não utilize a **Central de Atualizações**, o patch da Release 1.4.1 (ou superior) deve ser aplicado. Ele é imprescindível pois atualizará o **RPO** com a **nova interface e suas funcionalidades**;*

**Passo 2:** 

Aplique os patchs de **Expedições Contínuas** dos módulos relacionados abaixo para atualizar o **RPO** com os pacotes **ZSPS** e também as **rotinas vinculadas aos processos de stored procedures**, os pacotes estão disponíveis em [Stored Procedures - Novo gerenciador de pacotes](https://tdn.totvs.com/x/FqDXJg)

***IMPORTANTE:*** *Os patchs de **Expedição Contínua** dos módulos são necessários para que o **RPO** seja atualizado com os pacotes de procedures no novo formato **.ZSPS**, além das rotinas associadas às stored procedures. A aplicação destes patchs **é obrigatória**, caso contrário poderão ocorrer erros durante a **instalação/desinstalação** de processos.*

**Passo 3:** 

Acesse o programa **Gerenciador de procedures**, através do menu **Base de Dados | Dicionário | Stored Procedure**. Será apresentada a seguinte interface:  
![](https://tdn.totvs.com/download/attachments/651665430/worddavc93595b23c3aa2e2ab88c0fd823d291b.png?version=1&modificationDate=1637355052587&api=v2)

***IMPORTANTE:*** *Esta interface contendo as opções será apresentada somente se o patch da **Central de Atualizações Release 1.4.1 (ou superior)** foi aplicado corretamente no ambiente;*

As opções disponíveis são:

* **Documentação:** ao clicar neste botão o usuário será levado para esta documentação.
* **Manter:** ao clicar neste botão a rotina atual, sem as novas funcionalidades, será exibida. É importante lembrar que o modelo antigo não sofrerá nenhuma atualização, isto é, não serão expedidas atualizações em arquivos SPS, somente no novo formato ZSPS.
* **Atualizar:** ao clicar neste botão, ocorrerá o processo de migração. Serão realizados procedimentos que não poderão ser desfeitos, ou seja, após migrado não será possível voltar ao modelo antigo de gestão de procedures. Após realizada a migração para o novo modelo essa interface de migração não será exibida novamente.
* **Fechar:** a rotina não será acionada, retornando ao menu da janela principal do Protheus.

**Passo 4:** 

Clique no botão **Atualizar**. O processo de migração se inicia e ao ser concluído a nova interface será apresentada.

Para **Instalar ou Desinstalar Stored Procedures** através do Novo Gestor de Stored Procedures (CFGX051M), acesse:

* [Instalando pacotes de Stored Procedures](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28150721529623-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Instalando-pacotes-de-Stored-Procedures)
* [Desinstalando pacotes de Stored Procedures](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28150699874071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Desinstalando-pacotes-de-Stored-Procedures)
* [Processo no antigo Gestor de Stored Procedure](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28150717052439-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-no-antigo-Gestor-de-Stored-Procedure)

**Saiba mais:**

[*Stored Procedures utilizadas no produto Estoque e Custos*](https://tdn.totvs.com/x/wi3AFQ)

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
