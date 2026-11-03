---
article_id: 360022005311
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f1e9688a5f67673ef90d82f0bc7680a1fd1029c4eca51cae2cfe1e632ed54579
fetched_at: '2026-06-28T22:38:53.873984+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  MATA175 - HELP A175LIB
  Problema: Quantidade a ser liberada/rejeitada inválida'
type: support-article
updated_at: '2025-12-10T12:45:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022005311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA175-HELP-A175LIB-Problema-Quantidade-a-ser-liberada-rejeitada-inv%C3%A1lida
---

O HELP A175LIB ocorre na liberação de C.Q quando a quantidade a liberar é maior que o saldo na tabela SD7, causado por saldo insuficiente, saldo negativo, controle por endereço ou lote/endereço. Verifique as casas decimais, saldos nas unidades de medida e use o relatório MATR282 para divergências. Se persistir, envie dados ao suporte, como Inspetor de Objetos, arquivo SX3, pilha de chamadas, pontos de entrada e origem do movimento.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34420999227671) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**  
Ao efetuar Liberação de C.Q apresenta o HELP A175LIB - Problema: Quantidade a ser liberada/rejeitada inválida. Quais as principais causas?

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34420973598359)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

Este HELP está relacionado à liberação da Baixa ser maior que o saldo constante na tabela SD7.

**Solução**   
A rotina **MATA175** realiza validações específicas para a exibição do **HELP A175LIB** em situações que envolvem controle de quantidades e saldos de estoque. As principais ocorrências são:

1. **Quantidade superior ao saldo disponível:**  
   Quando a quantidade digitada na **1ª unidade de medida** for maior que o saldo.

   > Observação: este saldo pode estar convertido em função da **2ª unidade de medida**, sendo necessário validar se os saldos das unidades estão consistentes.
2. **Saldo negativo:**  
   Quando a quantidade digitada no campo **Saldo** resultar em valor negativo (considerando ambas as unidades de medida).
3. **Controle por endereço:**  
   Quando a quantidade informada for maior que o saldo existente no **endereço**, nos casos em que o produto controla endereço.
4. **Endereço sem estoque:**  
   Quando o endereço informado não possuir saldo disponível.
5. **Controle por lote/endereço:**  
   Quando o produto possuir controle de **lote** e/ou **endereço**, é necessário validar se não há **desbalanceamentos**, por meio do relatório **MATR282**. [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR282 - Parametrização para validar divergência de saldos SB2 x SB8 x SBF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-validar-diverg%C3%AAncia-de-saldos-SB2-x-SB8-x-SBF)

### **Observações Importantes**

* As comparações são realizadas com base nas **casas decimais** do campo **D7\_QTDE**.
* É imprescindível que os campos decimais estejam **devidamente configurados e equiparados**. Caso contrário, recomenda-se fortemente ajustar a configuração de decimais.
* Atualmente, existe o recurso [**Grupo de Campos Numéricos**](https://tdn.totvs.com/x/JVo9L) para auxiliar nessa adequação.
* Em situações mais críticas, pode ser necessário avaliar cada campo individualmente via **Configurador**.
* **Atenção:** não é permitido **reduzir** a quantidade de decimais de um campo — apenas **aumentar**. O próprio sistema bloqueia reduções.
* Caso haja a necessidade de ajustes estruturais, recomenda-se o acompanhamento de um **analista especializado em base de dados (in loco)** para a devida correção dos campos e respectivas **pictures**.

***Dica:*** *Revise na FAQ abaixo os cenários em que precisou alterar a  Segunda Unidade de Medida dos produtos e se forma efetuados os ajustes como indicado.*  
[***Como incluir saldo na 2° Unidade de Medida de produto com saldo?***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012683462-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-incluir-saldo-na-2-Unidade-de-Medida-de-produto-com-saldo?source=search)

### **Orientações em caso de persistência do HELP**

Após validar todas as ações previamente descritas, caso o **HELP** ainda seja exibido, siga os procedimentos abaixo e colete os dados para envio ao suporte.

1. **Inspetor de Objetos e Central de Diagnósticos**

   * Envie ao suporte o [**Inspetor de Objetos**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061655993-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-gerar-o-Inspetor-de-Objetos-no-Protheus) e um **print** da [**Central de Diagnósticos**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico).
2. **Arquivo SX3**

   * Anexe o arquivo **SX3** filtrado pelos seguintes campos:

     + **B2\_QATU /** **B2\_QTSEGUM /** **D7\_SALDO e** **D7\_QTSEGUM**
3. **Pilha de Chamadas**

   * No momento em que o **HELP** for exibido em tela, capture e encaminhe ao suporte o **print da Pilha de Chamadas**, conforme instruções do boletim: [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O que fazer quando aparecer um HELP na rotina?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33992870078615-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-O-que-fazer-quando-aparecer-um-HELP-na-rotina)
4. **Pontos de Entrada (PE)**

   * Verifique se existe algum **Ponto de Entrada (PE)** ativo na rotina.
   * Realize o teste **sem o PE** e informe ao suporte se havia PE e se o teste foi reproduzido sem ele, para liberação da análise.
5. **Origem do Movimento**

   * Especifique ao suporte a **origem do movimento** que gerou o saldo no armazém de CQ.
   * Informe claramente qual processo originou o saldo, por exemplo: documento de entrada, transferência, ajuste etc.
6. **Parâmetro MV\_CQ**

   * Certifique-se de que o parâmetro **MV\_CQ** esteja configurado com o **armazém de qualidade correto**.

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
