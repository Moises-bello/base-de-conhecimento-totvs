---
content_hash: 083f1c73391aee62a35a62e8c252b0631f0b9fd03925f0ec34696b78a9bf27a9
fetched_at: '2026-06-29T00:10:38.805203+00:00'
page_id: '545232022'
product: rm
source: tdn-rm
title: Parametrização para o Fracionamento de Jobs para o processo de Geração da Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=545232022
version: 4
---

Em RH | Folha de Pagamento | Ambiente | Segurança de Jobs Fracionáveis:

Definir um Perfil e Classe de Job para que a parametrização seja realizada com sucesso. Será necessário definir qual o perfil irá possuir autorização para executar o processo:

**Observação:** Deverá ser selecionada em Classe de Job a classe de processo ‘**FopRotinasContabilizacaoProcess**’.

Em RH | Folha de Pagamento | Encargos | Contabilização | Geração dos Lançamentos, será apresentado a opção o quadro de “**Escalabilidade**”, onde será possível definir a quantidade de fracionamentos do processo:

Após realizar a parametrização e executar o processo de Contabilização, serão criados os Jobs em RH | Folha de Pagamento | Ambiente | Gerenciamento de Jobs:

**Observação:** Neste módulo, serão apresentados os Jobs referentes a execução do processo.

**Exemplo: No quadro abaixo, o processo foi executado em 06 (seis) Jobs, no entanto foram apresentados 07, pois o job 617891 foi responsável pelo o gerenciamento dos 06 (seis) Jobs filhos.**

**Veja também outros fracionamentos:**

* [Agendamento com fracionamento jobs](https://tdn.totvs.com/display/LRM/Agendamento+com+fracionamento+jobs)
