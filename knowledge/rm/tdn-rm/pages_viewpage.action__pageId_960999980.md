---
content_hash: fd5ed321eac503a96a471a5015e98c9d633dbe77772e91ea7e42f54d71300fe0
fetched_at: '2026-06-29T00:12:13.931176+00:00'
page_id: '960999980'
product: rm
source: tdn-rm
title: Parametrização para o Fracionamento de Jobs para o processo de Agrupamento
  de Lançamentos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=960999980
version: 4
---

**01. VISÃO GERAL**

     Esse documento trata do fracionamento no processo de agrupamento de lançamentos contábeis, para maiores informações sobre o funcionamento do processo acesse: [Agrupamento de Lançamentos Contábeis](https://tdn.totvs.com/pages/viewpage.action?pageId=423938653)  
  
      O fracionamento de Jobs tem por função otimizar o tempo e recurso de processo, porém, é necessário atender algumas premissas para obter um maior ganho de desempenho, como por exemplo, possuir hosts distribuídos, para isso, é necessário que o ambiente esteja configurado em [N camadas](https://tdn.totvs.com.br/pages/viewpage.action?pageId=236432384).

**02. EXEMPLO DE CONFIGURAÇÃO**

Adicione na configuração do host as tags:

    <add key="IsolateProcess" value="true" />  
    <add key="EnableProcessIsolation" value="true" />  
  
Habilite o processamento de Jobs em Gerenciamento de Alias.

Em BackOffice| Gestão Contábil | Ambiente | Segurança de Jobs Fracionáveis:

Definir um Perfil e Classe de Job para que a parametrização seja realizada com sucesso. Será necessário definir qual o perfil irá possuir autorização para executar o processo:

**Observação:** Deverá ser selecionada em Classe de Job a classe de processo ‘**CtbAgrupaLancamentosData**’. Para maiores informações acesse [Segurança - Fracionamento de Jobs](https://tdn.totvs.com.br/pages/viewpage.action?pageId=547231277)

Ao acessar o processo em BackOffice| Gestão Contábil | Escrituração Contábil| Lotes| Agrupamento de Lançamentos Contábeis , será apresentado a opção o quadro de “**Escalabilidade**”, onde será possível definir a quantidade de fracionamentos do processo:

Após realizar a parametrização e executar o processo de Agrupamento de Lançamentos, serão criados os Jobs em Ambiente | Gerenciamento de Jobs:

**Observação:** Neste módulo, serão apresentados os Jobs referentes a execução do processo.

**Exemplo: No quadro abaixo, o processo foi executado em 7(sete) Jobs, no entanto foram apresentados 8(oito), pois o job 5105917 foi responsável pelo o gerenciamento dos 7(sete) Jobs filhos.**
