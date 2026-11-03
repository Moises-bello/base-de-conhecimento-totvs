---
content_hash: 9908a3d39b74b09c08e98007f57a3161f9af3a6d7465bd7e6276a579c1137d9b
fetched_at: '2026-06-29T00:08:10.583420+00:00'
page_id: '240306876'
product: rm
source: tdn-rm
title: RMCTB00001_Orientação sobre Inconsistência do centro de custo ECD X ECF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240306876
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Contábil |
| **Versões:** | 12.1.17 |
| **Ocorrência:** | Orientação sobre Inconsistência do centro de custo ECD X ECF |
| **Ambiente:** |  |
| **Passo a passo:** | **Regra de acordo com a ECF:**  Como regra a ECF valida que se uma conta contábil tem movimentação para um determinado centro de custo esta mesma conta não pode ter movimentação sem centro de custo.  **Regras de acordo com o SPED Contábil:**  Já o SPED Contábil não aplica a mesma validação da ECF, ou seja, caso uma conta contábil tenha movimentação com centro de custo esta mesma conta contábil **pode ter** movimentação sem centro de custo.  **Importante:**  Ressaltamos que o centro de custo é uma informação gerencial e que o usuário poderá optar em não enviar, para isto basta acessar o cadastro de centro de custo e desmarcar a opção ““Enviar para o SPED Contábil”, porém se o usuário optar em enviar o centro de custo todas as movimentações que se enquadra na regra: ***“Caso uma conta contábil tenha movimentação com centro de custo esta mesma conta contábil não deveria ter movimentação sem centro de custo”***deverão ter o centro de custo preenchido.  Quando temos a situação de termos a ECD sem centro de custo e ECF com centro de custo, nos deparamos com as seguintes mensagens:  **Observação:**  Recomendamos queao recuperar o arquivo da ECD mantenha a opção em destaque desmarcada, pois a ECF gerada pelo RM já preenche informações do registro K155, K355.    Se a opção em destaque estiver marcada e o usuário não enviou na ECD o plano de contas referencial e seus respectivos mapeamentos ou existir divergência no mapeamento referencial em função do centro de custo, será apresentado o erro abaixo:    Se a opção em destaque estiver desmarcada (recomendado), ao recuperar o arquivo da ECD para ECF podem ser apresentadas advertências em relação ao registro E155 (gerado a partir do arquivo da ECD) com K155.    Observação: Advertência não impede o envio do arquivo.  **Lembrando:**  Isso ocorre quando na ECF é recuperado o arquivo da ECD nas seguintes situações:  - O cliente entregou a ECD sem ajustar a movimentação conforme as regras relatadas acima , porém ao entregar a ECF ajustou a movimentação de sua base.  - Após a entrega da ECD o cliente realizou algum ajuste nas movimentações e que irão impactar nos centros de custos.    **Eliminando a advertência/erro**   * Ajustar as movimentações da base de dados que se enquadre na regra  ***“Caso uma conta contábil tenha movimentação com centro de custo esta mesma conta contábil não deveria ter movimentação sem centro de custo”***   **Ajustando as Movimentações**   * Se o usuário optar em não enviar o centro de custo basta acessar o cadastro de centro de custo e demarcar a opção “Enviar p/ SPED”.   É importante avaliar esta opção juntamente com o contador da empresa, pois uma vez enviado o centro de custo, logo este ano também deverá ser enviado, principalmente em casos que a ECF anterior também é recuperada.   * Se o usuário optar em ajustar as movimentações, poderá utilizar a ferramenta de preenchimento de centro custo desenvolvida como facilitador.   Acesse o menu: Escrituração Contábil/Ferramentas/Preenchimento do Centro de Custo nas Movimentações (Regra SPED/ECF)   * Após os ajustes citados acima execute o processo de associação dinâmica do centro de custo com o plano de contas referencial.   *<http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.PlanoContaParaleloAssociacaoDinamica.aspx>*   * Gerar a ECD novamente já com as movimentações ajustadas, deverá proceder com a substituição. * Gerar a ECF novamente recuperando o arquivo da ECD contendo as movimentações ajustadas. |
| **Observações:** | Preferencialmente execute o processo acima em base de homologação primeiramente e após validar o resultado final, execute em base oficial. |
