---
content_hash: 1d8498f173d7b8b3b13af3a8e7299bb5335c11f278937f7e1b305f7e68202126
fetched_at: '2026-06-29T00:09:17.628927+00:00'
page_id: '421388611'
product: rm
source: tdn-rm
title: Imprimir Cheques
type: documentation
url: https://tdn.totvs.com/display/LRM/Imprimir+Cheques
version: 7
---

A impressão de cheques é realizada através do Assistente de Impressão de Cheques (menu Processos da janela de visão do cadastro). O assistente pode ser utilizado através dos módulos de Extratos de Caixa.  
É possível imprimir um cheque ou vários cheques ao mesmo tempo.

**Gerador de Relatórios**

Ao selecionar o modo de impressão "gerador de relatórios" você pode utilizar relatórios criados através do RM Reports.

**Impressora de Cheques**

Ao selecionar o modo de impressão "impressora de cheques" você pode utilizar várias impressoras de cheques que já possuem um layout de impressão configurado internamente no TOTVS Gestão Financeira.  
As impressoras disponíveis são:

* Bematech DP 20-Plus
* CheckPlus CS100
* Check Pronto ACC100
* mprecheq NSC 2.01
* Quattro Easy AP40RW 2E
* TSP Slip 80
* Pertochek 501S
* Imprecheq NSC 2.18 - Elgin

Para efetivar a impressão de cheques no RM FLUXUS, desde a versão 10.0, não é necessária nenhuma configuração ou instalação de softwares de terceiros. Ou melhor, não se devem instalar os softwares do próprio fabricante para gerenciar a impressão. Isto evitará conflitos. Para realizar a impressão, basta 'plugar' a impressora na porta COM 1 ou COM 2 da máquina.   
Com relação o acesso via Terminal Service (TS), existe uma solução com relação às impressoras que serão instaladas localmente num ambiente de TS, que é uma ferramenta chamada 'jetro cockpit' (esta ferramenta já foi testada pela TOTVS, mas é um fabricante externo). As configurações deste tipo de impressão devem ser realizadas na ferramenta de TS. Neste caso, deve-se entrar em contato com a empresa responsável pelo acesso via TS e verificar os recursos disponíveis.

**Observação**

Para impressora Imprecheq NSC 2.18 – Elgin é necessário alterar o parâmetro Bits Parada (Stop Bits) para 2, pois o padrão do parâmetro é Bits Parada igual a 1.

**Banco**

O layout de impressão a ser utilizado dependerá do número do banco informado.

**Texto do Verso do Cheque**

Você pode incluir no parâmetro "Verso do Cheque" (Assistente de Implantação de Processos | processo: Manutenção de Baixa | etapa: Recebimento / Pagamento em Cheque) informações para serem impressas no verso do cheque. Estas informações serão apresentadas por default quando você marcar a opção "Imprimir Verso do Cheque" no Assistente de Impressão de Cheques. É possível colocar no texto informações de alguns campos do cheque, para isso, utilize as variáveis do TOTVS Gestão Financeira.

**Reimpressão de Cheque**

Você pode permitir ou não a reimpressão de cheque utilizando o parâmetro "Reimprimir Cheque" (Assistente de Implantação de Processos | processo: Baixa | etapa: Recebimento / Pagamento em cheque).

Veja Também
