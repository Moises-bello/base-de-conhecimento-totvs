---
content_hash: f71d1381eb871d508fd62b36dba725a8eeec2e1e0a6b5c4762a2bce313c8388c
fetched_at: '2026-06-29T00:11:28.302070+00:00'
page_id: '73074416'
product: rm
source: tdn-rm
title: Emissão Boleto via JOB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=73074416
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Gerador de Relatórios                      **Versão:**11.10 |
| **Processo** | **:** | Criação de um Boleto para geração pelo Portal |
| **Subprocesso** | **:** | Configuração de um Boleto para ser impresso por JobServer no Portal Educacional |
| **Data da publicação** | **:** | 26/07/2013 |

**Criação** **do Relatório** **TOTVS Gestão** **Financeira**

1. Criação de Fórmulas a serem usadas no Relatório para Geração de IPTE e Código de Barras

***Acesse: Cadastro*** ***/Fórmulas***

Fórmula para geração de IPTE Texto:

***IPTEBOLETO*** ***(-1)***

Fórmula para geração de Código de Barras

Texto:

***CODBARRABOLETO*** ***(-1)***

Obs. Código e Título das Fórmulas são livres, nomes como IPTE e CodBarra, são recomendados pois são de fácil localização, para inserção das fórmulas no relatório, conforme será mostrado posteriormente.

2. Criação do Relatório a ser utilizado para impressão do boleto no Portal

***Acesse: Relatório*** ***/ Gerador***

Campo Código: Livre sugerido (Boleto Web)

Campo Descrição: Livre sugerido (Boleto Banco XXXX Web) Flag: Nível de Acesso: ***1***

***CheckBox:*** ***Executa*** ***em*** ***JobServer deve ser marcado***

***Campo*** ***Tipo*** ***do*** ***Relatório:*** ***BOLETO Campo Tipo*** ***de saída:*** ***PADRÃO***

Inserção da Linha de Detalhe, clicar no campo marcado de Azul.

Insira a LD, clicar na LD – Linha de Detalhe e na seta Azul, depois em OK.

Clique em Relatório, Ok

Linha inserida no Grupo de Relatórios, Clicar em OK   
 Criada a LD 01.   
   
   
   
 Clique com o Botão direito do mouse, Inserir Fórmulas   
   
   
   
   
 Insira a Fórmula para Geração de IPTE.

Clique duas vezes no campo onde a Fórmula (Campo circulado em Azul) foi inserida e formate a apresentação da mesma.

Insira a Fórmula para geração de Código de Barras

Clique duas vezes no campo onde a Fórmula (Campo circulado em Azul) foi inserida e formate a apresentação da mesma, atente para o guia formatação onde a categoria sempre deve ser "***Código de Barras".***

Obs: As Fórmulas inseridas são somente para geração de IPTE e Código de Barras, os campos da tabela FLAN (CODCOLIGADA, IDLAN E IDBOLETO) são obrigatórios.

Insira os filtros obrigatórios para impressão do boleto pelo portal, os filtros devem ser inseridos conforme print abaixo. ***Coligada*** ***=*** ***VAZIO*** ***ID*** ***do*** ***boleto*** ***=*** ***VAZIO***

3. Acesse o TOTVS Educacional, para configuração do Boleto.

***Acesse: Parâmetros/*** ***Educacional***

Selecione o Boleto criado, no TOTVS Gestão Financeira.

Caso o relatório de boleto não esteja aparecendo verifique os passos da pagina: 03 e 07 itens de Tipo de Relatório, Tipo de Saída e Filtros obrigatórios.

4. Parametrização Alias.DAT para habilitar processamento de Job   
 Acesse o Executor e clique em "Gerenciar Alias".

Marque o CheckBox Habilitar Processamento de Job, esta opção pode ser marcada em várias máquinas.

6. Configure o arquivo .config

Configure o arquivo RM.Host.Service.exe (Arquivo CONFIG), o mesmo se encontra na pasta de instalação do Sistema em: C:\totvs\CorporeRM\RM.Net conforme tela abaixo

Configuração a ser feita no arquivo: Edite o arquivo e crie a seguinte tag:

<add key="JobServer3Camadas" value="true"/> Veja a tela abaixo

As alterações devem ser feitas em todas as maquinas que o *Alias* estiver habilitado para processar Job's.

Após alterações o arquivo **\_*Brocker.DAT*** deve ser apagado e o mesmo se encontra em ***C:\totvs\CorporeRM\RM.Net***.

6. Pare o serviço para criação do Arquivo \_Brocker.DAT

***Acesse: Iniciar / Executar*** ***(RUN)***

Digite: Services.msc

Localize o Serviço: ***RM.HOST.SERVICE*** e clique com o botão direito no Mouse em propriedades

Pare o Serviço e depois inicie o Serviço

7. Acesse o Portal Educacional

Acesse a área acadêmica

Clique em Financeiro   
   
 Clique na opção "Extrato Financeiro".

Clique na impressora para a emissão do Boleto

A mensagem abaixo mostra a emissão de Boleto realizada com sucesso.

|  |  |
| --- | --- |
|  | **Para maiores informações:**  Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)    **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha). |
