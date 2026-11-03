---
article_id: 21382225710487
category: Originação de Grãos (OG)
content_hash: e3efca2f2cb2b471ae56db59df40163f206c79efac279eb14ac733823f97ec9f
fetched_at: '2026-06-28T22:45:39.395047+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Excedente de Volume no Contrato
type: support-article
updated_at: '2025-04-07T20:59:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21382225710487-Agro-Linha-Protheus-AGR-Excedente-de-Volume-no-Contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21382249179031) Tempo aproximado para leitura: **00:03:10 min  
  
Dúvida**O que fazer para realizar um **Excedente de Volume no Contrato**? **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12 **Solução**Para solucionar essa dúvida, realize os seguintes passos:

Para o contrato de compra e venda, no caso do volume exceder a quantidade contratada é possível definir como se deseja atuar para que o processo de recebimento ou expedição não pare.

**1.** Verifique no **Gestão Agroindústria** **-** **SIGAAGR**, acessando em **Atualizações > Originação > Controle Fiscal > Motivo Alter. Ctr. - OGA140**;

**a.** Cadastre um motivo com a opção **Excedente = Sim.  
  
2.** Acesse **Atualizações > Originação > Controle de Venda > Contrato de Venda - OGA290**.

**a.** Cadastre um contrato com o campo **Exceder Vol? = Última carga**.

**3.** Acesse **Atualizações > Originação > Comercialização > Romaneio com Pesagem - OGA250**;

**a.** Informe um romaneio cuja quantidade seja superior a quantidade do saldo do contrato. Efetue a pesagem e atualização do romaneio.

**b.** Será criado uma alteração do tipo Adição para o contrato e o romaneio será atualizado com sucesso

* **% de tolerância**
* **Opção** **Exceder Vol? 3 - Percentual**:

**4.** Verifique no modulo **Gestão Agroindústria - SIGAAGR**, acesse **Atualizações > Originação > Controle de Compras > Contrato de Compras - OGA280**. Crie um novo contrato, marque a opção **Exceder Vol?** com o valor **3 - Percentual** e informe o percentual tolerável de excedente para o contrato no campo **Tol. Entrega**;

![EX.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21382225683991)

**5.** Verifique no modulo **Gestão Agroindústria (SIGAAGR),** acesse **Atualizações > Originação > Comercialização > Romaneio C/pesagem - OGA250**. Atualizando os romaneios, o Sistema verifica o peso liquido e se for menor ou igual a quantidade tolerável de acordo com o percentual, é criado um aditivo no contrato com o peso liquido do romaneio, ou com a diferença após ser zerado o saldo do contrato;   
  
**Exemplo:**Criar contrato de compra com quantidade 100.000,00, tolerância de entrega 10% (Max. 110.000,00) e Exceder Vol? 3 - Percentual;

Criar 3 romaneios com pesagem com peso liquido 34.300,00 (102.900,00), o Sistema deve gerar um aditivo de 2.900,00;

O contrato passa ser de 102.900,00;

Criar mais um romaneio com peso liquido 34.300,00, o Sistema bloqueia a atualização do romaneio pois a quantidade excedente (27.200,00) ultrapassa a quantidade permitida no contrato (110.000,00);

Neste caso, se forem gerados romaneios com até 7.100,00 o Sistema gera novos aditivos com o peso liquido do romaneio até atingir o máximo permitido para o contrato (110.000,00), ou seja a soma dos aditivos não pode ultrapassar os 10.000,00 (10%).

Caso permita, ao registrar um romaneio em que o volume exceder o do contrato, o Sistema irá gerar um aditivo no contrato. Na verificação do saldo excedente na atualização dos romaneios será considerado a quantidade física ou fiscal de acordo com o definido no tipo de controle do contrato.

|  |  |
| --- | --- |
| **Rotina** | **Nome Técnico** |
| **OGA290** | **Cadastro de Contrato de Venda** |
| **OGA280** | **Cadastro de Contrato de Compra** |
| **OGA250** | **Romaneio com Pesagem** |
| **OGA251** | **Romaneio Sem Pesagem** |
| **OGA335** | **Alteração de Contrato** |

**6.** Visualize o romaneio que originou a aditação excedente do contrato, para verificar o romaneio que originou a aditação deve seguir os passos abaixo:

**a.** Acesse **Atualizações > Originação > Comercialização > Alteração Contrato - OGA335**;  
**b.** Clique em Visualizar para consultar o registro de Aditação gerado para o contrato, cujo valor será a diferença entre a quantidade do romaneio e o saldo do contrato;  
**c.** Verifique na tela de visualização, clicar em **Ações Relacionadas > Consultar Romaneio** para visualizar o romaneio que gerou o excedente;  
  
**7.** Atualize a quantidade excedente da Autorização, em ambos os casos anteriores **Exceder Vol? 2 e 3** ao gerar os aditivos o Sistema também atualiza as quantidades das autorizações **OGA335** e as quantidade autorizadas de entrada ou de saída do contrato **Qt.Autz.Ent., Qt.Autz.Sai.**, são somados aos valores iniciais as quantidades dos adicionais.  
  
**8.** Reabra o Romaneio, em ambos os casos anteriores **Exceder Vol? 2 e 3** ao reabrir o romaneio o Sistema verifica se existe aditivos de contrato vinculado ao romaneio, caso houver, o aditivo será excluído e o Sistema atualiza as quantidades de autorizações e saldos do contrato.  
Define se é permitido exceder o volume do contrato na entrega do romaneio. E caso seja permitido, se o volume entregue pelo romaneio poderá exceder de acordo com o percentual de tolerância do contrato ou apenas na última carga entregue;  
  
**9.** Veja em ambos os casos, caso exceda o volume permitido será gerado aditivo no contrato.

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

**-> Inclusão automática de Saldo de 5.000. Saldo do contrato: 0.000.**

**3ª Entrega: 2.000. -> Não será permitido a entrega.**
