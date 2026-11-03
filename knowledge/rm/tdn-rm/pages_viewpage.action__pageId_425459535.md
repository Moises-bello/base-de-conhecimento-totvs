---
content_hash: a5cfece0515a79f811450a2d05eb30d6f539e1ad6f06447d2c3c67d6ad5c96f3
fetched_at: '2026-06-29T00:09:36.869132+00:00'
page_id: '425459535'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Processo de Transferência de Pneus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459535
version: 2
---

**Backoffice RM x Protheus SigaMNT - Processo de Transferência de Pneus**

---

O Protheus SigaMNT permite a transferência de Bens do tipo Pneu  entre  as filiais, passando por um fluxo de Transferência até o  Recebimento.   
    
   
 O processo de transferência é definido em três etapas, descritas abaixo:  
    
 **1.**        **Solicitação de transferência**  
                a.        A solicitação de transferência não efetua nenhuma movimentação de estoque, não disparando nenhuma mensagem de integração.  
    
 **2.**        **Remessa de Pneus**  
               a.        Quando alguma filial atende a solicitação de transferência de pneus é gerada uma remessa de pneus.  
               b.        A remessa de pneus gera uma baixa de estoque na filial de origem, sendo assim enviada uma mensagem de baixa de estoque ao BackOffice.  
    
 **3.**        **Recebimento de Pneus**  
              a.        Ao receber o pneu originado por transferência é necessário informar este recebimento na devida rotina para que a solicitação seja finalizada e o produto tenha entrada no estoque.  
              b.        A rotina de recebimento de pneus gera um acréscimo de estoque na filial recebedora, originando uma mensagem de entrada em estoque no BackOffice.

O Protheus sigaMNT  possui duas funcionalidades responsáveis por gerenciar a transferência de pneus , conforme descritas abaixo.

* Remessa de Pneus

                    o    Ao atender a uma solicitação de transferência, a filial de origem efetua a remessa de pneus para a filial de destino, gerando assim uma baixa em seu estoque.

* Recebimento de Pneus

                    o    Ao efetuar o recebimento de um pneu a filial de origem executa a rotina referente no módulo SigaMNT Frotas, gerando assim acréscimo em seu estoque.  
  
**Pré - Condições  :**  
  
 1.     Inserir um estoque em um produto  no Backoffice RM.  
 2.     Sincronizar um  Produto com estoque    do Backoffice RM  para o Protheus  SigaMNT.  
 3.     Sincronizar  um Local de Estoque do Backoffice RM  para o Protheus  SigaMNT.  
 4.     Sincronizar uma Condição de Pagamento do Backoffice RM  para o Protheus SigaMNT.  
 5.     Sincronizar  um Centro de Custo do Backoffice RM  para o Protheus SigaMNT.   
 6.     Configurar o parâmetro MV\_NGMNTFR com o  valor S  
 7.     Configurar tipos de movimento de baixa de estoque e de acréscimo de estoque no BackOffice RM   
 8.     Configurar os parâmetros de integração "TMVBaixa" e "TMVEntradaEstoque" com os códigos dos tipos de movimento de saída e entrada em estoque.  
 9.     Sincronizar um  Ativo Fixo do Backoffice RM para o Protheus SigaMNT.  
 10.  Alterar o Ativo Fixo para a Categoria Pneu e vinculá-lo a o produto com estoque  sincronizado.

**O Fluxo a seguir é executado  ao executar o processo de Transferência de Pneus :**

1. Incluir  uma transferência  no Protheus SigaMNT referênciando um  Bem (Ativo Fixo) do tipo Pneu e que  esteja a vinculado a um produto no Backoffice RM com estoque.
2. É enviada uma mensagem    de Baixa de estoque  do Protheus SigaMNT ao  Backoffice RM
3. É gerado um movimento de baixa de estoque no Backoffice RM que  retira   uma unidade  do Local de Estoque  vinculado ao produto  informado no cadastro do Bem(Ativo Fixo).
4. O Estoque do produto  é  decrementado conforme  especificado no movimento de Baixa de estoque criado.
5. Incluir um Recebimento   no Protheus SigaMNT referenciando a Transferência  gerada no início do processo de Transferência de Pneus.
6. É enviada uma mensagem de entrada de estoque  do Protheus SigaMNT ao Backoffice RM.
7. É gerado um movimento de Entrada de estoque no Backoffice RM que inclui o bem transferido  no local de estoque da filial que está recebendo o Bem(Ativo Fixo).

---

Para mais informações sobre o processo de Transferência de Pneus, acesse os boletins técnicos.

**Recursos Adicionais**

TDN - Boletim Técnico : [Processo de Transferência de Pneus](http://tdn.totvs.com/download/attachments/76251261/PROTHEUS_BT_TRANSFER%c3%8aNCIA+DE+PNEUS_BR_CON000158.pdf?version=1&modificationDate=1380053414000)
