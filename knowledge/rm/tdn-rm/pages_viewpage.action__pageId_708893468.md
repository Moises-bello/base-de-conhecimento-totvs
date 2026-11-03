---
content_hash: 318eedf1906e5fb7302897cd81cc18607ffa75a9e3f19820825ed05aca7648dc
fetched_at: '2026-06-29T00:11:25.476899+00:00'
page_id: '708893468'
product: rm
source: tdn-rm
title: Parametrização para o Fracionamento de Jobs para o processo  Integrar Lote(s)/Lançamento(s)
  ao Lote Oficial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=708893468
version: 1
---

**01. VISÃO GERAL**

     Esse documento trata do fracionamento no processo de integração de lotes/lançamentos ao lote oficial, para maiores informações sobre o funcionamento do processo acesse: [Integrar Lote(s)/Lançamento(s) ao Lote Oficial](https://tdn.totvs.com.br/pages/editpage.action?pageId=286747991)  
  
      O fracionamento de Jobs tem por função otimizar o tempo e recurso de processo, porém, é necessário atender algumas premissas para obter um maior ganho de desempenho, como por exemplo, possuir hosts distribuídos, para isso, é necessário que o ambiente esteja configurado em [N camadas](https://tdn.totvs.com.br/pages/viewpage.action?pageId=236432384).

**02. EXEMPLO DE CONFIGURAÇÃO**

Adicione na configuração do host as tags:

    <add key="IsolateProcess" value="true" />  
    <add key="EnableProcessIsolation" value="true" />  
  
Habilite o processamento de Jobs em Gerenciamento de Alias.

Em BackOffice| Gestão Contábil | Ambiente | Segurança de Jobs Fracionáveis:

Definir um Perfil e Classe de Job para que a parametrização seja realizada com sucesso. Será necessário definir qual o perfil irá possuir autorização para executar o processo:

**Observação:** Deverá ser selecionada em Classe de Job a classe de processo ‘**CtbLoteIntegracaoData**’. Para maiores informações acesse [Segurança - Fracionamento de Jobs](https://tdn.totvs.com.br/pages/viewpage.action?pageId=547231277)

Ao acessar o processo em BackOffice| Gestão Contábil | Escrituração Contábil| Lotes| Integrar Lote(s)/Lançamento(s) ao Lote Oficial , será apresentado a opção o quadro de “**Escalabilidade**”, onde será possível definir a quantidade de fracionamentos do processo:

Após realizar a parametrização e executar o processo de Contabilização, serão criados os Jobs em RH | Folha de Pagamento | Ambiente | Gerenciamento de Jobs:

**Observação:** Neste módulo, serão apresentados os Jobs referentes a execução do processo.

**Exemplo: No quadro abaixo, o processo foi executado em 10(dez) Jobs, no entanto foram apresentados 11(onze), pois o job 10816 foi responsável pelo o gerenciamento dos 10(dez) Jobs filhos.**
