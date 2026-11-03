---
content_hash: 13da2b058f4916b438c30cbe65c8c6358f3d862146d30753ea0b1c523b0429c5
fetched_at: '2026-06-29T00:08:12.735221+00:00'
page_id: '243648044'
product: rm
source: tdn-rm
title: COT0002_Incluir_Item_em_uma_Ordem_de_Compra_de_um_Fornecedor_ja_existente
type: documentation
url: https://tdn.totvs.com/display/LRM/COT0002_Incluir_Item_em_uma_Ordem_de_Compra_de_um_Fornecedor_ja_existente
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.82.42 e superiores |
| **Ocorrência:** | Movimento não exibido durante o processo de incluir item em uma ordem de compra de um fornecedor já existente |
| **Ambiente:** | Cotação - Incluir item em uma ordem de compra de um fornecedor já existente |
| **Passo a passo:** | Ao executar o processo para gerar Ordem de Compra a partir de uma cotação, marcando a opção “**incluir item em uma Ordem de Compra de um fornecedor já existente**” conforme print      o movimento de Ordem de Compra desejado não é exibido na tela de “**Escolha de Movimento Existente**”, como mostrado abaixo:       CAUSA  1. O status da ordem de compra está diferente de “Pendente”; 2. O código do Cliente/Fornecedor é diferente do ganhador da cotação; 3. O campo “Status de Mov. de Compras” está com um valor diferente de “Gerado por Cotação”; 4. O movimento já foi impresso; 5. Já foi enviado e-mail desta movimentação; 6. Existem lançamentos financeiros baixados relacionados à movimentação; 7. O movimento possui contabilidade; 8. A movimentação já encontra-se aprovado.  SOLUÇÃO Com as consultas abaixo, conseguirá identificar todas essas informações:  SELECT   STATUS, – Deve estar como 'A', ou seja, 'Pendente'   MOVIMPRESSO, – Deve estar como '0', 'Não impresso'   STSEMAIL, – Deve estar como '0', e-mail não enviado   STSCOMPRAS, – Deve estar como 'G', que corresponde a 'Gerado por Cotação'   CODCFO – Este código deve ser o mesmo do Cli/For vencedor da cotação FROM TMOV WHERE IDMOV = XXXX AND CODCOLIGADA = X  **-- Caso exista, o lançamento financeiro não pode estar baixado (STATUSLAN=1)**  SELECT STATUSLAN, \* FROM FLAN WHERE IDMOV=XXXX AND CODCOLIGADA=X  **-- Movimento NÃO pode ter gerado contabilidade**  SELECT \* FROM TMOVCTB WHERE IDMOV=XXXX AND CODCOLIGADA=X  **-- Não pode ter aprovação**  SELECT \* FROM TMOVAPROVA WHERE IDMOV=XXXX AND CODCOLIGADA=X    Caso a movimentação em questão apresentar qualquer informação conflitante com os dados descritos acima a mesma não será apresentada durante o processo. Faça a verificação e a correção da situação deste(s) movimento(s) para que o(s) mesmo(s) seja(m) devidamente apresentado(s).    **IMPORTANTE**    Não recomendamos alterações via banco de dados, sendo assim se o movimento está, por exemplo, com um lançamento financeiro baixado, o que faz com que ele não seja exibido neste processo, o mesmo deverá ser retornado para o status 'em aberto' através dos processos nativos do sistema, neste caso o cancelamento da baixa.  Caso mesmo após proceder com todas as verificações descritas acima o incidente persista, entre em contato com nossa equipe de suporte e estaremos prontos para atendê-lo. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
