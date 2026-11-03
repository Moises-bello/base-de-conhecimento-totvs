---
content_hash: f80767d48224e377f0cad8ed7c7f08b81bba70b98878a33ac33006c03fdd3224
fetched_at: '2026-06-29T00:08:37.017572+00:00'
page_id: '284862347'
product: rm
source: tdn-rm
title: Definir Servidor JOB Exclusivo
type: documentation
url: https://tdn.totvs.com/display/LRM/Definir+Servidor+JOB+Exclusivo
version: 5
---

# Definir Servidor JOB Exclusivo

|  |  |
| --- | --- |
| **Produto:** | TOTVS RM |
| **Versões:** | 12.1.XX ou Superiores |
| **Ocorrência:** | Definir servidor JOB exclusivo para um servidor aplicação |
| **Ambiente:** | Cockpit |
| **Passo a passo:** | Objetivo Esta pagina tem por objetivo, apresentar um passo a passo para auxiliar a configuração de servidor JOB exclusivo para um servidor aplicação. Introdução Ao marcar um servidor de JOB como exclusivo para um servidor de Aplicação, estará definindo que todos os processos deste servidor de Aplicação serão executados somente pelo servidor de Jobs selecionado.  Caso o ambiente tenha outros servidores de aplicação, é necessário manter pelo menos um servidor de Job sem exclusidade configurada para execução de jobs. Esta ferramenta, está disponível somente em ambientes N camadas;Passo a Passo   1. Acesse o módulo Serviços Globais, na aba Ambiente, selecione o menu Cockpit; 2. Em nosso exemplo temos dois servidores:   BHD050100591 = Servidor de Aplicação  JOB\_Server = Servidor de JOB     3. A configuração deve ser realizada no servidor de JOBs;  3.1. No campo Servidores de Aplicação, insira o nome do servidor de Aplicação;    3.2. Clique em salvar e Reinicie o Host do servidor de JOB.   Reiniciar o Host Para reiniciar o serviço **RM.Host.Service**, siga os passos abaixo:   1. Acesse o caminho **UNIDADE:\totvs\CorporeRM\RM.Net**; 2. Clique com o botão direito do mouse em **RM.Host.ServiceManager.exe** e selecione a opção **Executar como Administrador**; 3. Marque a Flag **Apagar \_Broker.dat** e clique em **Desativar**; 4. Quando o status estiver como “**Parado**”, Clique em **Iniciar** e aguarde até que o status esteja como “**Iniciado**”.  Quando realizar o processo acima em servidor de Aplicação, todos os usuários irão “deslogar” automaticamente, pois o serviço será reiniciado. |
| **Observações:** |  |
