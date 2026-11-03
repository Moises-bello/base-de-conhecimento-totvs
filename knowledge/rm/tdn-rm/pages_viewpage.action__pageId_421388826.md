---
content_hash: afe12b49b1449d5ba76e5a63488778a7aba84cfb8d208273f10ae066593cd06f
fetched_at: '2026-06-29T00:09:19.210321+00:00'
page_id: '421388826'
product: rm
source: tdn-rm
title: Diagnóstico das Contabilizações Financeiras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388826
version: 3
---

O recurso "Diagnóstico das contabilizações Financeiras" tem o objetivo de validar/corrigir inconsistências nas operações contábeis geradas a partir  dos Lançamentos Financeiros e de operações manuais no Extrato de Caixa,  gerenciados pelo TOTVS Gestão Financeira.  Por segurança, este recurso será apresentado na tela a cada acesso ao sistema até que o mesmo seja executado,  e,  se não for confirmada a sua execução, para ter acesso novamente basta acessar o menu "Utilitários".

É possível que a duplicidade de operações contábeis tenha maior impacto nos processos de "Alteração Global de Eventos Contábeis do Lançamento" e na inclusão de Lançamentos e/ou registos manuais de extrato de Caixa pelo recurso Copiar/Colar .  
 Este processo contempla:

* Lançamentos dos Tipos "Contábil",  "Baixa Contábil"  com status  "Não Cancelados" e com a contabilização realizada pelo modelo novo da Contabilidade.
* Registros manuais inseridos no Extratos de Caixa  do Tipo "Contábil" e com status "Não cancelados" e com a contabilização realizada pelo modelo novo da contabilidade.

**Atenção!**

* Fazer cópia de segurança e executar o processo,  inicialmente,  em ambiente e base de testes.
* O processo só pode ser executado por usuário que tenha atribuições de perfil definidas para "Supervisor", porém é permitido aos demais,  verificar a existência de operações contábeis inconsistentes.

**Processo**

* A partir do release 11.52.55, ao acessar o sistema será apresentado o wizard do processo.
* Para execução do processo de diagnóstico da base, será preciso informar um período para que sejam validados os Lançamentos e/ou  os registros manuais no Extrato de Caixa e selecionados os registros com inconsistências. Este período irá considerar a "Data de Contabilização".
* O usuário com perfil de Supervisor deverá selecionar o registro e executar o processo para que a correção seja feita automaticamente. Esta correção será realizada indiferente do lote contábil em que o registro esteja inserido, inclusive no lote zero.
* Ao final do processo será apresentado um log de processamento informando a situação de cada Lançamento.

**Efeito**

As  referências das operações contábeis serão recriadas mantendo a integridade da informação financeira x contábil.

**Observação**

No TOTVS Gestão Contábil, Utilitários foi disponibilizado o menu: Diagnóstico de rastreabilidade dos Lançamentos Contábeis, cujo objetivo é identificar e corrigir inconsistências, assim como duplicidade de contabilização e possíveis operações contábeis sem rastro, mantendo a integridade de cada operação contábil.
