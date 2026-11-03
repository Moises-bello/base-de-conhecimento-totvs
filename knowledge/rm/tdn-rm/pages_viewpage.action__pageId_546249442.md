---
content_hash: 47b015d3f7303c4eafdc74cfbb61a7c203fe81b2282a69149111468fcc45219c
fetched_at: '2026-06-29T00:10:39.570086+00:00'
page_id: '546249442'
product: rm
source: tdn-rm
title: TAF - Como gerar as bases de INSS/FGTS/IRRF no relatório do eSocial do futuro?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546249442
version: 13
---

false

**A partir das Versões:**

* 12.1.26.211
* 12.1.27.163
* 12.1.28.101
falseImportante

* Para a utilização do novo relatório do TAF do futuro é imprescindível a atualização e configuração do pacote. Mais informações [clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=528452172)

Será necessário algumas configurações para realizar a geração do relatório.

1) Realize a configuração do DefaultDB. Informações em : 

2) Acesse o menu Serviços Globais| Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em Acesso a Menus e permita o acesso 09.06.01 Api's Relatório Conferência INSS/FGTS

Importante

Nas versões e patches iguais e superiores a 12.1.28.147, 12.1.27.237 e 12.1.26.255 é imprescindível a execução do sistema RM.Atualizador.exe para a criação da tabela PESOCIALTOTALIZADORESAUTONOMOS, que será utilizada no relatório de conferência de INSS para comparação dos autônomos cadastrados no TOTVS Gestão Financeira ou autônomos externos. 

A partir da 12.1.29 não é necessário executar o RM.Atualizador.exe.

3) Após acesse o módulo SIGACFG e siga o passo a passo:

Vá em Ambiente | Cadastros | Parâmetros e cadastre as informações nos seguintes parâmetros:

* **MV\_TAFRHLG :**Este parâmetro deve ser preenchido com o usuário do sistema de RM.

* **MV\_TAFRHPW:**Senha do usuário do sistema RM preenchido no parâmetro acima.

* **MV\_TAFRHUR:**URL do Software do sistema RM. Este endereço, geralmente composto por IP + ApiPort do host, será responsável por armazenar a API que será consumida para o produto obter as bases dos valores do relatório.

Mais informações em: .

4) Após o envio de sua folha ao eSocial (evento S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social) pelo modulo SIGATAF.

Acesse Miscelânea | eSocial | eSocial do Futuro

E gere o relatório normalmente com as informações. Mais detalhes em [Novo eSocial ( Versão 2.5 e Simplificada )](https://tdn.totvs.com/pages/releaseview.action?pageId=528917450)
