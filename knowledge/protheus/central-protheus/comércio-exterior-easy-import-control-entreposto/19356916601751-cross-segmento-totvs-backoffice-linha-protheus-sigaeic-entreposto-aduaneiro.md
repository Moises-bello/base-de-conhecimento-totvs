---
article_id: 19356916601751
category: Comércio Exterior - Easy Import Control - Entreposto
content_hash: 055cf6ac670b5e64ce6857dd522263dc44b46534ea7ff10ba4f31a7db517b1d0
fetched_at: '2026-06-28T22:39:46.059722+00:00'
product: protheus
section_id: 1500001549622
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Entreposto Aduaneiro.
type: support-article
updated_at: '2023-11-27T19:07:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19356916601751-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Entreposto-Aduaneiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19356931283479) Tempo aproximado para leitura: **05:00 min** **Dúvida**Como o Entreposto Aduaneiro é tratado no SIGAEIC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  –*Easy Import Control*– Todas versões.  
  
**Solução****Entreposto Aduaneiro dentro do SIGAEIC:**

**![](https://tdn.totvs.com/download/attachments/281260523/image2017-6-21%2019%3A24%3A45.png?version=1&modificationDate=1498084780000&api=v2)**

**DA (Declaração de Admissão)**

Segue a mesma rotina de um processo normal, porém, nunca vai haver o desembaraço (DI) e sim uma Declaração de Admissão (DA).  
De acordo com o Decreto nº 6759 Art. 407. É permitida a admissão no regime de mercadoria importada com ou sem cobertura cambial.  
A DA pode ter a condição de pagamento com ou sem cobertura cambial, condição essa que deve ser invertida no processo de nacionalização.  
Para as DAs com cobertura cambial será gerado parcelas de câmbio durante o e para as DAS que a condição de paramento é sem coberta essas parcelas não serão geradas.  
Também não é possível excluir uma DA, caso seu embarque tenha gerado um PO. (Nacionalização).

![](https://tdn.totvs.com/download/attachments/281260523/image2017-6-21%2019%3A25%3A19.png?version=1&modificationDate=1498084780000&api=v2)

**Declaração de Importação Nacionalização**

Serão incluídos automaticamente após a rotina de nacionalização a SN (Solicitação de Nacionalização (SI)), o PN (Pedido de Nacionalização) e a LI (os produtos que forem anuentes no cadastro e não tiverem anuência na DA estarão no PN como anuente, caso o produto esteja como anuente na DA este será gravado como não anuente no PN), na exclusão do PO deve ser excluído a SI, não podendo ser excluído itens do PO.  
A diferença entre Declaração de Transito Aduaneiro e Declaração de Transito Aduaneiro Simplificada, é que na simplificada a mercadoria não fica na INFRAERO vai direto ao armazém do importador com isto o importador não paga nada de armazenagem para INFRAERO.  
Pré–Requisitos:  
- Possuir o P.O. com saldo.  
- Incluir um embarque com o P.O. requisitado.

**DESEMBARAÇO**  
O lançamento dos dados no Desembaraço é fundamental importância para realização de controles gerenciais como custos.  
Exemplo – Como incluir um processo de Desembaraço:  
1. Selecione as opções “Atualizações\Desembaraço\Manutenção”.  
2. Localize o processo desejado e clique na opção “Alterar” e na pasta Cadastrais, informe os seguintes dados: Tipo Declar = 02 - Admissao em entreposto aduaneiro

3. Selecione a pasta “Embarque” e informe os dados necessarios para seguir.

4. Selecione a pasta “Transporte” e confira os dados de frete e seguro.  
5. Na pasta “Valores DI” informe os seguintes dados: Taxa US$ DI

Obs.: Os campos inibidos serão calculados automaticamente pelo sistema.  
6. Selecione a pasta “DI” e informe os dados para registro.

7. Clique sobre o botão “Itens”, o sistema apresentará a tela para seleção de itens (PO/PLI).

8. Em “Ações Relacionadas” clique em “Invoices”, na tela de manutenção de invoices em “Ações Relacionadas” clique em “Incluir”. Preencha as informações a seguir e clique em “Confirmar” para gravar.  
Observação: Neste exemplo a condição de pagamento do processo de embarque/desembaraço esta sem cobertura cambial, lembrando que é possível incluir uma condição de pagamento com cobertura no processo.  
9. Clique sobre o botão “Próxima tela”, o sistema apresentará a tela de conferência final.

10. Confira os dados e clique sobre o botão “Confirmar” para gravar.

**PREPARANDO DADOS PARA NACIONALIZAÇÃO**  
É necessário acionar esta rotina, após o Desembaraço, confeccionado em regime de Admissão em Entreposto Aduaneiro, para que o sistema crie automaticamente um PN (pedido de nacionalização) com todo o desembaraço. O SIGAEIC irá utilizar o No. da DA (informado no Desembaraço) para numerar o campo de referência do pedido de nacionalização.

**Exemplo – Como preparar os dados para nacionalização:**

1. Selecione as opções “Atualizações\Entreposto\Prep. Dados Nacion.”.  
2. Posicione no processo desejado e clique na opção “Admissão” e informe os dados.

3. Selecione a pasta “Transporte” e informe os dados.

4. Selecione a pasta “Financeiro” e informe os dados.

5. Note que na parte inferior o número da DA é o mesmo digitado na capa do Desembaraço.

6. Confira os dados e clique sobre o botão “OK” para gravar. Com isto é gerado um pedido de nacionalização cópia do processo de embarque da DA.

**PEDIDO DE NACIONALIZAÇÃO**  
Esta rotina deve ser acionada para que se façam modificações no pedido, assim como visualização de saldo dos itens.

**DESEMBARAÇO DE NACIONALIZAÇÃO**  
Após a criação do pedido de nacionalização, o usuário poderá criar quantos desembaraços desejar, respeitando o saldo a receber daquele produto do pedido de nacionalização.

**Exemplo – Como incluir o desembaraço de nacionalização:**

1. Selecione as opções “Atualizações\Entreposto\Desemb. Nacional.”.  
2. Clique na opção “Incluir” e informe o número do processo de nacionalização e do pedido de nacionalização.

3. Clique no botão “Confirmar” para prosseguir.  
4. Repare que é apresentada a tela com os dados preenchidos no Desembaraço.  
5. Na pasta “Cadastrais”, informe os dados a seguir: Tipo Declar: 14 - NACIONALIZAÇÃO DE ENTREPOSTO ADUANEIRO

6. Na pasta “DI”, informe os dados.

7. Em seguida, clique no botão “Itens” no campo “No. P.O.” informe o numero do Pedido de Nacionalização.

Atenção: O número do PO que deve ser informado nesta etapa é o número do pedido de nacionalização gerado após a Admissão do Entreposto. Este número sempre começará com “DA”.  
8. Clique no botão “Confirmar” para continuar.  
9. O sistema apresentará a tela para seleção de itens. Dê um duplo clique no item.

10. Verifique se está tudo correto e clique no botão “OK”.  
11. Para incluir as invoices, clique em “Ações Relacionadas” e escolha a opção “Invoices” o sistema apresentará a tela de manutenção de invoices.  
12. Na tela de invoices em “Ações Relacionadas” clique sobre a opção “Incluir” e informe os dados.

**Saiba mais:****[Entreposto Aduaneiro](https://tdn.totvs.com/display/public/PROT/EIC0012_Entreposto)**
