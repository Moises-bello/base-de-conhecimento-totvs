---
article_id: 360045923434
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 63a1af0256c7e1bea805c529e38d786629ee22510b53018d46807f80cc885df5
fetched_at: '2026-06-28T22:40:44.650226+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD  EMPRESA CONSOLIDADORA
  COMO GERAR REGISTROS I350 - I355 - I150 - I155 '
type: support-article
updated_at: '2023-02-02T12:51:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045923434-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-EMPRESA-CONSOLIDADORA-COMO-GERAR-REGISTROS-I350-I355-I150-I155
---

**Dúvida**

* Como gerar os registro da ECD [I350 - I355 - I150 - I155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016508952-MP-SIGACTB-ECD-N%C3%83O-GERA-REGISTROS-I350-I355-I150-I155?source=search) na empresa Consolidadora
* Criei empresa em meu sigamat um Empresa/Filial consolidadora para gerar a ECD e posteriormente executei a rotina de [CTBA220 ou CTBA231](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014649651-MP-SIGACTB-Documenta%C3%A7%C3%A3o-Consolida%C3%A7%C3%A3o-CTBA220-CTBA231?source=search), agora os registro I350 - I355 - I150 - I155 não estão sendo gerados

**Ambiente**  
Protheus – Contabilidade Gerencial  – A partir da versão 11.80

**Requisitos**

* Caso tenha gerado a ECD com [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search) verifique se o centro de custo está devidamente apurado , caso contrario será gerado o saldo errados no arquivo
* Apuração de resultado devera ser feita pelo sistema (inclusive a apuração da conta transitória para conta de patrimônio,caso possua) . [Exemplo - Apuração Trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search) e [Exemplo - Apuração Anual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041555313-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Anual-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)
* Veja se o  [Nivel\_AGL está correto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048123714-MP-SIGACTB-ECD-J150-Nivel-AGL-N%C3%A3o-deve-existir-mais-de-uma-linha-de-n%C3%ADvel-igual-a-1-na-DRE?source=search)
* Veja se o  [VL\_CTA e COD\_AGL estão corretamente cadastrados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028548031-MP-SIGACTB-ECD-registro-J150-7-VL-CTA-e-2-COD-AGL?source=search)
* Veja como esta a **[ORDENAÇÃO RELATÓRIO (DRE e BALANÇO) X ECD (J00 e J150)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023832631-MP-SIGACTB-CTBA161-ORDENA%C3%87%C3%83O-RELAT%C3%93RIO-DRE-e-BALAN%C3%87O-X-ECD-J00-e-J150-?source=search)**
* Veja se o procedure da ECD [MV\_CTBSPRC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007132632-MP-SIGACTB-Habilitar-procedures-din%C3%A2mica-na-gera%C3%A7%C3%A3o-da-ECD?source=search) esta configurado
* Aplique [Pacote atualizado da ECD](https://suporte.totvs.com/portal/p/10098/download?e=955972) seguindo as instruções [Aqui descritas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025142372-MP-SIGACTB-Como-atualizar-o-ECD-?source=search)
* Aplique**o Pacote Acumulado Contábil + [Instalação de Procedure nele existente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011410951-MP-SIGACTB-SIGAATF-Instala%C3%A7%C3%A3o-de-Procedure-?source=search):**

  Obs : necessário aplicação deste pacote para que os fonte CTBXATU , CTBA190 e os demais fontes de atualização de saldo estejam atualizados
* Realize um reprocessamento de saldo, pois os registro são gerado com base na tabelas de saldo

**Solução**

Caso tenha criado em seu sigamat um empresa/ filial consolidadora para gerar a ECD e tenha executado a rotina de Consolidação [CTBA220 ou CTBA231](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014649651-MP-SIGACTB-Documenta%C3%A7%C3%A3o-Consolida%C3%A7%C3%A3o-CTBA220-CTBA231?source=search)necessário verificar :

* Nas "Filiais Origem" não execute a [Apuração de resultados CTBA211](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472-MP-SIGACTB-Como-realizar-Apura%C3%A7%C3%A3o-de-resultados-dentro-do-Protheus-?source=search), pois as contas de Receita e Despesas devem ser levadas para a empresa/Filial Consolidadora com saldo.
* Caso tenha realizar a apuração de Resultado na Filiais Origem é necessário realizar o [estorno de apuração de resultados (CTBA215).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010708171-MP-SIGACTB-ECF-Como-realizar-estorno-de-apura%C3%A7%C3%A3o-de-resultados-L-P-?source=search) para posteriormente realizar a consolidação para a Consolidadora (Empresa/Filial Destino)
* Caso tenha executada a consolidação com as contas de Receita e Despesa já apuradas na filial Origem necessário realizar :  
    
  **1º Passo**
* Através da rotina CTBA215 realize nas Filiais Origem o[estorno de apuração de resultados (Clique Aqui, para verificar todos os passos a serem conferidos)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010708171-MP-SIGACTB-ECF-Como-realizar-estorno-de-apura%C3%A7%C3%A3o-de-resultados-L-P-?source=search)  
    
  **2º Passo**
* Realize a Consolidação [CTBA220 ou CTBA231](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014649651-MP-SIGACTB-Documenta%C3%A7%C3%A3o-Consolida%C3%A7%C3%A3o-CTBA220-CTBA231?source=search)para a Consolidadora (Empresa/Filial Destino)
* Configure a pergunta "Limpa consolidadora=SIM”?"
* Após realizar a consolidação confira através de relatórios(CTBR040,CTBR400) se os saldos de todas as contas contábeis foram levados para consolidação corretamente, ao concluir que esta correto o saldo na consolidadora siga com o **3º Passo**  
    
  **3º Passo**
* Realize a [Apuração de resultados CTBA211](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472-MP-SIGACTB-Como-realizar-Apura%C3%A7%C3%A3o-de-resultados-dentro-do-Protheus-?source=search) nas Filiais Origem
* Realize a [Apuração de resultados CTBA211](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005048472-MP-SIGACTB-Como-realizar-Apura%C3%A7%C3%A3o-de-resultados-dentro-do-Protheus-?source=search) na Consolidadora (Empresa/Filial Destino)  
    
  **4º Passo**
* Após conferir que as contas forma apuradas corretamente nas Filiais Origem e na Consolidadora (Empresa/Filial Destino) gere o arquivo da ECD através da empresa Consolidadora

Saiba Mais :

* [NÃO GERA REGISTROS I350 - I355 - I150 - I155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016508952-MP-SIGACTB-N%C3%83O-GERA-REGISTROS-I350-I355-I150-I155?source=search)
* [ECD PRÉ-REQUISITOS PARA GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028834291-MP-SIGACTB-ECD-PR%C3%89-REQUISITOS-PARA-GERAR-?source=search)
* [Como atualizar o ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025142372-MP-SIGACTB-Como-atualizar-o-ECD-?source=search)
* [Exemplo - Apuração Anual : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041555313-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Anual-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)
* [Exemplo - Apuração Trimestral : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)
