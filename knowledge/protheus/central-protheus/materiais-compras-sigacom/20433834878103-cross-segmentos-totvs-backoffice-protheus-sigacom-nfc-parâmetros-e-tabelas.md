---
article_id: 20433834878103
category: Materiais - Compras (SIGACOM)
content_hash: 06ca8e546f97fcaab611cec3ab1f1598eda631952829c4e8a9013be9308bef84
fetched_at: '2026-06-28T22:41:21.882862+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Parâmetros e
  Tabelas
type: support-article
updated_at: '2026-03-02T18:34:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20433834878103-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Par%C3%A2metros-e-Tabelas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20433834863383) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Quais são os Parâmetros e Tabelas utilizados pelo NFC - Novo Fluxo de Compras ?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

**Tabelas :**

* DHU (Cabeçalho da Cotação)
* DHV (Produtos da Cotação)
* SA2 (Fornecedores)
* SB1 (Descrição Genérica do Produto)
* SC1 (Solicitações de Compra)
* SC8 (Cotações)
* AC9 (Relação de Objetos x Entidades)
* ACB (Bancos de Conhecimentos)
* SCE (Encerramento de Cotações)
* SC7 (Pedido de Compra)

**Parâmetros :**

* **MV\_PGCWF** - Permite utilizar o e-mail do comprador para enviar o formulário de workflow ao fornecedor.
* **MV\_SELFOR** - Permite o comprador escolher os fornecedores livremente ou somente dentre os amarrados no Produto x Fornecedor.
* **MV\_PCEXCOT** - Habilita a reabertura da cotação ao excluir um Pedido de Compra ou Contrato.
* **MV\_TPPLA** - Tipo da planilha a ser utilizado ao gerar um contrato proveniente da cotação.
* **MV\_APIFOR** - Habilita o preenchimento automático de dados do fornecedor com a API TOTVS Carol (Utilizado preenchendo o CNPJ ao transformar participante da cotação em fornecedor)
* **MV\_PGCPISV**- Servidor de e-mail POP 3/ IMAP dos compradores.
* **MV\_PGCPIPO**- Porta de e-mail POP 3/ IMAP dos compradores.
* **MV\_PGCSMSR**- Servidor de e-mail SMTP dos compradores.
* **MV\_PGCSMPO**- Porta de e-mail SMTP dos compradores.
* **MV\_PGCTAUT**- Tipo de autenticação do servidor de e-mail: TLS, SSL ou nenhum.
* **MV\_COTFIAP** - Em caso de cotação com compra centralizada, os pedidos serão gerados na filial de entrega ou filial de compra.
* **MV\_GRIMPWF** - Informa se deve calcular o IPI e ICMS-ST (mesmo zerado no workflow), de acordo com os valores do sistema, ou considerar apenas os valores vindos do Workflow. O parâmetro é do tipo lógico. Situação: Resposta do workflow do fornecedor com valores de IPI e ICMS-ST **zerados:** **.T.** - Sistema calculará os valores e gravar nos respectivos campos SC8 / **.F.** - Sistema não calculará os valores e os respectivos campos continuarão zerados.
* **MV\_PGCOBC1** - A observação da SC1 deve ser carregada na Cotação e PC, no NFC? .T. - Para Sim / .F. - Não (default)
* **MV\_NFCMOED** - Parâmetro que verifica se o cadastro da moeda será utilizado da tabela CTO ou do parâmetro MV\_MOEDA, onde 1=CTO(Default) / 2=MV\_MOEDA
* **MV\_CALQIPI -** Parâmetro que desabilita o recálculo automático do percentual e valor de IPI, onde ao ficar com o valor **.T.** (**True**), o sistema não vai recalcular automaticamente os valores e alíquotas de IPI; e o valor **.F.** (**False**), indica que o sistema deve fazer o padrão, ou seja, recalcular automaticamente quando a alíquota ou valor for alterados, conforme o sistema atua hoje. O default do parâmetro é .F., ou seja, manter o recálculo dos campos de alíquota e valor de IPI automáticos.
* **MV\_NFCDTRE -** Permite alterar o prazo de recebimento da cotação .T. = Ativado; .F. = Desativado (Se parâmetro ativo, o botão para alteração aparecerá na tela de edição da cotação)***.***
* **MV\_NFCDESC -** Permite definir de qual tabela virá a descrição do produto no Novo Fluxo de Compras. 1=SB1; 2=SB5; 3=SC1.
* **MV\_DESQFPD -**Permite que, quando definido como **.T.** (**True**), faz com que, ao finalizar uma cotação com Pedido de Compra (PC) ou Contrato, todos os demais fornecedores que não responderam à cotação sejam automaticamente marcados como **desqualificados**.

Para maiores informações sobre o NFC acesse: [Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
