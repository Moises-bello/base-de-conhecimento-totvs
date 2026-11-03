---
article_id: 27627262400791
category: Originação de Grãos (OG)
content_hash: 6053c4019b71b925f284efaaba2debe3a5dca8115c2a2f7686a60c320926bb95
fetched_at: '2026-06-28T22:45:39.385408+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Excedente de Volume no Contrato
type: support-article
updated_at: '2025-06-25T14:56:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27627262400791-Agro-Linha-Protheus-AGR-Excedente-de-Volume-no-Contrato
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27627288916247)** Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como funciona um processo de **Excedente de Volume no Contrato**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para o contrato de compra e venda, no caso do volume exceder a quantidade contratada é possível definir como se deseja atuar para que o processo de recebimento ou expedição não pare.

Podendo ser: 

* Não permite exceder :   Não permite que seja ultrapassada a quantidade contratada.
* Última carga               : A última carga será   

  No contrato na opção **Exceder Vol? 2 - Última carga**:

  1. No Gestão Agroindústria **SIGAAGR**, acesse **Atualizações / Originação / Controle Fiscal / Motivo Alter. Ctr. - OGA140**;
     1. Cadastre um motivo com a opção **Excedente = Sim**.
  2. Acesse **Atualizações / Originação / Controle de Venda / Contrato de Venda - OGA290**;
     1. Cadastre um contrato com o campo **Exceder Vol? = Última carga**;
  3. Acesse **Atualizações / Originação / Comercialização / Romaneio com Pesagem - OGA250**;
     1. Informe um romaneio cuja quantidade seja superior à quantidade do saldo do contrato. Efetue a pesagem e atualização do romaneio.
     2. Será criado uma alteração do tipo Adição para o contrato e o romaneio será atualizado com sucesso
* % de tolerância

            Opção "Exceder Vol?" 3 - Percentual:

1. 1. No modulo **Gestão Agroindústria (SIGAAGR),** acesse **Atualizações / Originação / Controle de Compras / Contrato de Compras (OGA280).**
   2. Aocriar um novo contrato marque a opção **Exceder Vol?** com o **valor 3** - Percentual e informe o percentual tolerável de excedente para o contrato no campo **Tol. Entrega**:  
      ![](https://tdn.totvs.com/download/attachments/498720424/Percentual%20-%20Contrato%20de%20compra.png?version=1&modificationDate=1562097625337&api=v2)
   3. No modulo **Gestão Agroindústria (SIGAAGR),** acesse **Atualizações / Originação / Comercialização / Romaneio C/pesagem (OGA250).**
   4. Ao atualizar os romaneios, o Sistema verifica o peso liquido e se for menor ou igual a quantidade tolerável de acordo com o percentual, é criado um aditivo no contrato com o peso liquido do romaneio, ou com a diferença após ser zerado o saldo do contrato.   
      **Exemplo:**
      1. Criar contrato de compra com quantidade 100.000,00, tolerância de entrega 10% (Max. 110.000,00) e Exceder Vol? 3 - Percentual;
      2. Criar 3 romaneios com pesagem com peso liquido 34.300,00 (102.900,00), o sistema deve gerar um aditivo de 2.900,00;
      3. O contrato passa ser de 102.900,00;
      4. Criar mais um romaneio com peso liquido 34.300,00, o Sistema bloqueia a atualização do romaneio pois a quantidade excedente(27.200,00) ultrapassa a quantidade permitida no contrato(110.000,00);
      5. Neste caso, se forem gerados romaneios com até 7.100,00 o Sistema gera novos aditivos com o peso liquido do romaneio até atingir o máximo permitido para o contrato (110.000,00), ou seja a soma dos aditivos não pode ultrapassar os 10.000,00 (10%).

Caso permita, ao registrar um romaneio em que o volume exceder o do contrato, o sistema irá gerar um aditivo no contrato. Na verificação do saldo excedente na atualização dos romaneios será considerado a quantidade física ou fiscal de acordo com o definido no tipo de controle do contrato.

Uso :

|  |  |
| --- | --- |
| **Rotina** | **Nome Técnico** |
| OGA290 | Cadastro de Contrato de Venda |
| OGA280 | Cadastro de Contrato de Compra |
| OGA250 | Romaneio com Pesagem |
| OGA251 | Romaneio Sem Pesagem |
| OGA335 | Alteração de Contrato |

**3. Visualizar o romaneio que originou a aditação excedente do contrato:**

Para verificar o romaneio que originou a aditação deve seguir os passos abaixo:

1. Acesse **Atualizações / Originação / Comercialização / Alteração Contrato - OGA335**;
2. Clicar em Visualizar para consultar o registro de Aditação gerado para o contrato, cujo valor será a diferença entre a quantidade do romaneio e o saldo do contrato.
3. Na tela de visualização, clicar em **Ações Relacionadas > Consultar Romaneio para visualizar o romaneio que gerou o excedente**.

**4. Atualizar a quantidade excedente da Autorização:**

Em ambos os casos anteriores **Exceder Vol? 2 e 3** ao gerar os aditivos o Sistema também atualiza as quantidades das autorizações **OGA335** e as quantidade autorizadas de entrada ou de saída do contrato **Qt.Autz.Ent., Qt.Autz.Sai**., são somados aos valores iniciais as quantidades dos adicionais.

**5. Reabrir o Romaneio**

Em ambos os casos anteriores **Exceder Vol? 2 e 3** ao reabrir o romaneio o sistema verifica se existe aditivos de contrato vinculado ao romaneio, caso houver, o aditivo será excluído e o Sistema atualiza as quantidades de autorizações e saldos do contrato.

Define se é permitido exceder o volume do contrato na entrega do romaneio. E caso seja permitido, se o volume entregue pelo romaneio poderá exceder de acordo com o percentual de tolerância do contrato ou apenas na última carga entregue.

Em ambos os casos, caso exceda o volume permitido será gerado aditivo no contrato.

Exemplo (Última carga):

Volume do contrato: 50.000.

1ª Entrega: 40.000. -> Saldo do Contrato: 10.000.

2ª Entrega: 40.000. -> Saldo do Contrato: -30.000. (Excede 30.000). Será permitido a entrega.

-> Inclusão automática de Saldo de 30.000. Saldo do Contrato: 0.000.

3ª Entrega: 10.000. -> Não será permitido a entrega.

Exemplo (Percentual de Tolerância):

Volume do contrato: 50.000. Percentual: 10,00%.

1ª Entrega: 40.000. -> Saldo do Contrato: 10.000.

2ª Entrega: 15.000. -> Saldo do Contrato: -5.000. (Excede 10%). Será permitido a entrega.

->Inclusão automática de Saldo de 5.000. Saldo do contrato: 0.000.

3ª Entrega: 2.000. -> Não será permitido a entrega.

* Tabela NJR - Contrato

* Tabela NNQ - Motivo de Alteração de Contrato

* Tabela NNW - Alteração de Contrato
