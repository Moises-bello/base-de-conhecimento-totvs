---
article_id: 28660103014039
category: Originação de Grãos (OG)
content_hash: 9eb647faabb48d4702b38dd59411b4731b0914ea3c499ee5fe48669d50eabd75
fetched_at: '2026-06-28T22:45:39.406509+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Excedente de Volume no Contrato no Conceitual
  SIGAAGR
type: support-article
updated_at: '2025-06-25T14:57:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28660103014039-Agro-Linha-Protheus-AGR-Excedente-de-Volume-no-Contrato-no-Conceitual-SIGAAGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28660103004055) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como funciona um **Excedente de Volume no Contrato no Conceitual SIGAAGR**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para o contrato de compra e venda, no caso do volume exceder a quantidade contratada é possível definir como se deseja atuar para que o processo de recebimento ou expedição não pare.

**Podendo ser:**

* Não permite exceder :   Não permite que seja ultrapassada a quantidade contratada.
* Última carga               : A última carga será

No contrato na opção **"Exceder Vol?" 2** - Última carga:

No **Gestão Agroindústria - SIGAAGR, acesse Atualizações / Originação / Controle Fiscal / Motivo Alter. Ctr. - OGA140**.

**1.** Cadastre um motivo com a opção Excedente = Sim;

**2.** Acesse em **Atualizações / Originação / Controle de Venda / Contrato de Venda - OGA290**;

**3.** Cadastre um contrato com o campo **Exceder Vol? = Última carga**;

**4.** Acesse em **Atualizações / Originação / Comercialização / Romaneio com Pesagem - OGA250**;

**5.** Informe um romaneio cuja quantidade seja superior à quantidade do saldo do contrato. Efetue a pesagem e atualização do romaneio;

**6.** Veja será criado uma alteração do tipo **Adição** para o contrato e o romaneio será atualizado com sucesso;

* % de tolerância. Opção **"Exceder Vol?" 3 - Percentual**:

* + No modulo **Gestão Agroindústria - SIGAAGR**, acesse **Atualizações / Originação / Controle de Compras / Contrato de Compras - OGA280.**
  + Aocriar um novo contrato marque a opção **"Exceder Vol?"** com o valor 3 - Percentual e informe o percentual tolerável de excedente para o contrato no campo **"Tol. Entrega"**:

![IGAA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28661079963927)

**7.** Verifique no modulo **Gestão Agroindústria (SIGAAGR),** acesse **Atualizações / Originação / Comercialização / Romaneio C/pesagem - OGA250**;

**8.** Atualize os romaneios, o Sistema verifica o peso liquido e se for menor ou igual a quantidade tolerável de acordo com o percentual, é criado um aditivo no contrato com o peso liquido do romaneio, ou com a diferença após ser zerado o saldo do contrato.

**Exemplo:**

* Criar contrato de compra com quantidade **100.000,00**, tolerância de entrega **10%** **(Max. 110.000,00)** e **Exceder Vol? 3 - Percentual**;
* Criar 3 romaneios com pesagem com peso liquido **34.300,00 (102.900,00)**, o sistema deve gerar um aditivo de **2.900,00**;
* O contrato passa ser de **102.900,00**;
* Criar mais um romaneio com peso liquido **34.300,00**, o Sistema bloqueia a atualização do romaneio pois a quantidade excedente **(27.200,00)** ultrapassa a quantidade permitida no contrato **(110.000,00)**;
* Neste caso, se forem gerados romaneios com até **7.100,00** o Sistema gera novos aditivos com o peso liquido do romaneio até atingir o máximo permitido para o contrato **(110.000,00)**, ou seja a soma dos aditivos não pode ultrapassar os **10.000**.

Caso permita, ao registrar um romaneio em que o volume exceder o do contrato, o Sistema irá gerar um aditivo no contrato. Na verificação do saldo excedente na atualização dos romaneios será considerado a quantidade física ou fiscal de acordo com o definido no tipo de controle do contrato.

Uso :

|  |  |
| --- | --- |
| **Rotina** | **Nome Técnico** |
| OGA290 | Cadastro de Contrato de Venda |
| OGA280 | Cadastro de Contrato de Compra |
| OGA250 | Romaneio com Pesagem |
| OGA251 | Romaneio Sem Pesagem |
| OGA335 | Alteração de Contrato |

**Visualizar o romaneio que originou a aditação excedente do contrato:**

Para verificar o romaneio que originou a aditação deve seguir os passos abaixo:

1. Acesse em **Atualizações / Originação / Comercialização / Alteração Contrato - OGA335**;
2. Clique em **Visualizar** para consultar o registro de **Aditação** gerado para o contrato, cujo valor será a diferença entre a quantidade do romaneio e o saldo do contrato;
3. Na tela de visualização, clicar em **Ações Relacionadas > Consultar Romaneio** para visualizar o romaneio que gerou o excedente.

**Atualizar a quantidade excedente da Autorização:**

Em ambos os casos anteriores **(Exceder Vol? 2 e 3)** ao gerar os aditivos o sistema também atualiza as **quantidades das autorizações - OGA335** e as quantidade autorizadas de entrada ou de saída do contrato **(Qt.Autz.Ent., Qt.Autz.Sai.)**, são somados aos valores iniciais as quantidades dos adicionais.

**Reabrir o Romaneio**

Em ambos os casos anteriores **(Exceder Vol? 2 e 3)** ao reabrir o romaneio o sistema verifica se existe aditivos de contrato vinculado ao romaneio, caso houver, o aditivo será excluído e o Sistema atualiza as quantidades de autorizações e saldos do contrato.

Define se é permitido exceder o volume do contrato na entrega do romaneio. E caso seja permitido, se o volume entregue pelo romaneio poderá exceder de acordo com o percentual de tolerância do contrato ou apenas na última carga entregue.

Em ambos os casos, caso exceda o volume permitido será gerado aditivo no contrato.

**Exemplo (Última carga):**

**Volume do contrato: 50.000.**

**1ª Entrega: 40.000. -> Saldo do Contrato: 10.000.**

**2ª Entrega: 40.000. -> Saldo do Contrato: -30.000. (Excede 30.000). Será permitido a entrega.**

**-> Inclusão automática de Saldo de 30.000. Saldo do Contrato: 0.000.**

**3ª Entrega: 10.000. -> Não será permitido a entrega.**

**Exemplo (Percentual de Tolerância):**

**Volume do contrato: 50.000. Percentual: 10,00%.**

**1ª Entrega: 40.000. -> Saldo do Contrato: 10.000.**

**2ª Entrega: 15.000. -> Saldo do Contrato: -5.000. (Excede 10%). Será permitido a entrega.**

**->Inclusão automática de Saldo de 5.000. Saldo do contrato: 0.000.**

**3ª Entrega: 2.000. -> Não será permitido a entrega.**
