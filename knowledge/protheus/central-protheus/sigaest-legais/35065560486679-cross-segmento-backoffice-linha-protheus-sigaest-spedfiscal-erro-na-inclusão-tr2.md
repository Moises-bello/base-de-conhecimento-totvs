---
article_id: 35065560486679
category: SIGAEST - LEGAIS
content_hash: 4ad6af1a45046eb7dbe6ced9421c7cee9d22cf1485876d0ca322d3f51397b9be
fetched_at: '2026-06-28T22:38:51.890404+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SPEDFISCAL Erro na
  inclusão TR2: TOP Error - 19 - Invalid bind parameter size 4096'
type: support-article
updated_at: '2025-09-19T18:06:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35065560486679-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SPEDFISCAL-Erro-na-inclus%C3%A3o-TR2-TOP-Error-19-Invalid-bind-parameter-size-4096
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35065528877591) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao tentar gerar o SPEDFISCAL com o Bloco H em ambiente PostgreSQL, o sistema retorna "Erro na inclusão TR2: TOP Error - 19 - Invalid bind parameter size 4096"  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33 ou Superior.  
  
**Causa**  
Este erro pode ocorrer devido a alguns fatores, como por exemplo, atualizações, pontos de entrada e customizações e/ou configuração incorreta do ODBC, abaixo estaremos informando pontos para a avaliação e correção.  
  
**Solução**

1. **Banco de dados com versão não homologada;**  
     
   Durante nossa avaliação em alguns ambientes verificamos que o erro ocorria para versões PostgreSQL não homologadas para uso DBAcess, para esses casos a recomendação é efetuar a utilização do banco uma versão homologada para a correta comunição entre o Protheus e o Banco de Dados, segue abaixo uma documentação com os Bancos e versões homologados  
   [Banco de dados e versões Homologadas](https://tdn.totvs.com/display/tec/DBAccess+-+Banco+de+dados)
2. **Versões inferiores à 17 do Driver de ODBC para a plataforma Windows.**  
   Conforme informado na documentação acima, há um bug conhecido e relatado à comunidade do PostgreSQL na versão 16 do driver de ODBC para a plataforma Windows. Também notamos casos com versões inferiores à 16, por exemplo a 13, onde ocorria o erro. Por isso, **recomendamos a atualização do driver para a versão 17.00.0003 ou superior.**
3. **Configuração indevida no ODBC:**  
   Verificamos que, em ambientes que utilizam banco de dados PostgreSQL, é necessária maior atenção na configuração do ODBC. Neste caso, verifique como está a configuração do seu ODBC e se ela está conforme a documentação abaixo:  
     
   - [**Como criar uma fonte de dados ODBC para uso com PostgreSQL no Windows**](https://tdn.totvs.com/display/tec/DBAccess+-+Como+fazer+para+criar+uma+fonte+de+dados+para+uso+com+o+PostgreSQL+-+Windows)  
   - [**Como criar uma fonte de dados ODBC para uso com PostgreSQL no LINUX**](https://tdn.totvs.com/display/tec/DBAccess+-+Como+fazer+para+criar+uma+fonte+de+dados+para+uso+com+o+PostgreSQL+-+Linux)
4. **Fontes e artefatos desatualizados:**  
   Verificamos também que alguns casos foram corrigidos após a atualização dos fontes e artefatos, neste caso por gentileza, verifique se seu ambiente está devidamente atualizado, caso não efetue um teste em ambiente de Homologação com as atualizações a seguir:  
    [- Acumulado BackOffice conforme sua versão](https://tdn.totvs.com/x/2hgdHw)  
     
   - [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526)  
   - [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)  
   - [Smartclient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/search/searchAll) - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia](https://suporte.totvs.com/portal/p/10098/download#detail/1112221)  
   - [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)  
   - [Central de Atualizações](https://suporte.totvs.com/portal/p/10098/download?e=946864#000006/368/TFSC/)
5. **E se mesmo assim persistir?**  
   Caso ainda persistir, compreendemos que se faz necessário avaliar pontualmente seu caso. Sendo assim, por favor, nos envie:  
     
   - Erro.log gerado completo;  
   - Banco e versão que está utilizando;  
   - Versão do Drive do ODBC está utilizando;  
   - Print da configuração do seu ODBC;  
   - Video demonstrando os parâmetros utilizados na rotina;  
   - Inspetor de Objetos análise dos fontes envolvidos;

Saiba mais:

[*Clique aqui e saiba mais sobre Legais/Fiscais no Estoqu*e.](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)
