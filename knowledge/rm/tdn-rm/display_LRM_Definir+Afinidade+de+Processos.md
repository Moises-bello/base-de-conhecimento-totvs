---
content_hash: 9f1746e7f0a66e477b4dc1de7e16280342432c8423fc03cc6e7ab2a6ad73110d
fetched_at: '2026-06-29T00:08:36.976889+00:00'
page_id: '284861496'
product: rm
source: tdn-rm
title: Definir Afinidade de Processos
type: documentation
url: https://tdn.totvs.com/display/LRM/Definir+Afinidade+de+Processos
version: 6
---

# Definir Afinidade de Processos

|  |  |
| --- | --- |
| **Produto:** | TOTVS RM |
| **Versões:** | 12.1.XX ou Superiores |
| **Ocorrência:** | Como definir afinidade de processos |
| **Ambiente:** | Cockpit |
| **Passo a passo:** | Objetivo Esta pagina tem por objetivo, apresentar um passo a passo para auxiliar a configuração de afinidade de processos. Introdução Ao definir a afinidade de processos para um servidor, apenas aquele servidor de JOB executará este processo.   Se configurada a afinidade, o job server só executará Jobs que respeitam essa afinidade.  Necessário manter pelo menos um servidor de Job sem afinidade de processo para executar os demais processos. O processo para definir afinidade de processos, está disponível somente em ambientes em 3/N camadas;Passo a Passo  1. Selecionando qual o processo será definido com afinidade    1. Acesse a nova MDI (RM.exe);    2. Execute o processo que será usado;    3. Acesse o módulo Serviços Globais e abra a aba Ambiente;    4. Clique no menu Gerenciamento de JOBs, na visão que aparecer localize o JOB;    5. Copie o campo Classe do Processo; 2. Definindo a afinidade    1. Ainda no módulo Serviços Globais, na aba Ambiente, selecione o menu Cockpit;    2. Na visão do Cockpit localize o servidor de JOB. O campo Executar Processos ativo;    3. No grupo Processo clique no botão Adicionar e cole o código de Classe do Processo desejado (selecionado no Passo 1.e );    4. Clique em salvar e Reinicie o Host do servidor de JOB.    Reiniciar o Host Para reiniciar o serviço **RM.Host.Service**, siga os passos abaixo:   1. Acesse o caminho **UNIDADE:\totvs\CorporeRM\RM.Net**; 2. Clique com o botão direito do mouse em **RM.Host.ServiceManager.exe** e selecione a opção **Executar como Administrador**; 3. Marque a Flag **Apagar \_Broker.dat** e clique em **Desativar**; 4. Quando o status estiver como “**Parado**”, Clique em **Iniciar** e aguarde até que o status esteja como “**Iniciado**”.  Quando realizar o processo acima em servidor de Aplicação, todos os usuários irão “deslogar” automaticamente, pois o serviço será reiniciado. |
| **Observações:** |  |
