---
article_id: 4430116320151
category: Faturamento - Integrações
content_hash: bdaef8e7abb1cdde55abbcd02134edcb75bd56cbd877a489d8949fe51e490c9e
fetched_at: '2026-06-28T22:38:26.469661+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Faturamento - Integração Carol com
  Cadastro de Clientes '
type: support-article
updated_at: '2025-01-10T20:18:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4430116320151-Cross-Segmentos-Backoffice-Protheus-Faturamento-Integra%C3%A7%C3%A3o-Carol-com-Cadastro-de-Clientes
---

**Dúvida**Dúvidas frequentes sobre Integração do Cadastro de Clientes com a Carol.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat- A partir da 12.1.27.  
  
**Solução**Segue abaixo perguntas e respostas da Instalação e operação da Integração

**Instalação, personalização e atualização**

1) É preciso executar a atualização do UPDDISTR para usar a Integração API Carol ?

R : Somente para clientes que estão no release .27. Clientes do release .33 estão prontos para o uso do Api

2) Quais os fontes que sempre devem estar atualizados e onde atualizar ?

R : Os fontes são APIFORCLI, FATAPICGC e MATV030A.   
  
As atualizações dos fontes estão disponíveis no pacote de acumulados do modulo Faturamento no link abaixo

https://suporte.totvs.com/portal/p/10098/download#000006

Sugerimos que o pacote de acumulados do Modulo Compras também seja atualizado devido a possibilidade de integrar fornecedores (além de clientes)

3) De forma resumida, o que é necessário para o uso do API

R : Parâmetro MV\_APICCGC como .T. e gatilho padrão do Protheus no campo A1\_CGC atualizado (observe se o gatilho possui a regra M030APICGC())

4) O API já está funcionando, porém, gostaria de incluir/excluir campos na busca (personalizar a busca)

R : No momento não é possível personalizar a busca (não há pontos de entrada ou parâmetros adicionais).   
  
Caso seja uma solicitação pontual para adicionar algum campo que a empresa considere essencial será necessário a própria empresa realizar a solicitação no link abaixo

https://centraldeatendimento.totvs.com/hc/pt-br/community/topics/360001704573-TOTVS-Backoffice-Linha-Protheus-Faturamento-Faturamento

5) Parâmetro como .T., gatilhado existente na base, pacote de acumulado do modulo faturamento aplicado e o sistema não retorna dados de clientes pessoa física (CPF)

R : Não há consulta de CPF, somente de CNPJ

6) Parâmetro como .T., gatilho existente na base, pacote de acumulado do modulo faturamento aplicado e o sistema não retorna dados ao incluir o CNPJ

R : Verifique se há bloqueio de comunicação externa na empresa (firewall, anti-virus entre outros). É necessário comunicação com o domínio "carol.ai", conforme documentação abaixo

https://docs.carol.ai/docs/carol-connect-2c#requirements-server

Caso a empresa faça testes de comunicação com o domínio "carol.ai" e perceba que a operação não conclui, favor abrir um ticket para equipe TOTVS Labs  
  
7) Meus gatilhos não são executados automaticamente após o API preencher os dados  
  
Ao utilizar qualquer API Protheus o sistema passa pelo gatilho, porém, as informações da API sobrescrevem as informações do gatilho (são as últimas informações a serem gravadas).  
  
Sendo assim, por padrão Protheus de uso do API (e não só da API da Carol), não é possível que o gatilho grave a informação posterior a informação automática da API.  
   
Para que as informações sejam gravadas é necessário que o campo do gatilho seja digitado alguma informação para que sobrescreva a informação da Carol no campo a receber os dados.

**Consulta do CNPJ**

8) Todos os campos do cadastro de clientes vão ser preenchidos com o uso do API ?

R : Não, somente os campos que constam na documentação abaixo (desde que o conteúdo dos dados exista na receita)

https://tdn.totvs.com/pages/releaseview.action?pageId=592560209

9) Achei uma empresa no site da receita e o Protheus não encontrou o CNPJ, alguma informação não está sendo preenchida ou está trazendo informação errada (por exemplo o endereço)

R : O API não busca informações diretamente do site da receita. A TOTVS atualiza os dados pelo site da receita a cada 3 meses para um servidor interno, que é a base de onde os clientes realizam as pesquisa

Se necessário, entre em contato com Suporte TOTVS Labs para obter maiores informações sobre atualizações da base de consulta

10) O cadastro de clientes está funcionando corretamente, porém, o cadastro de fornecedores não funciona

R : O cadastro de fornecedores possui fonte, gatilho e parâmetro próprios (não é o mesmo do cadastro de clientes). Entre em contato com suporte Compras para que possa habilitar a busca dos fornecedores

11) Há informações básicas obrigatórias que não estão aparecendo na busca, como por exemplo, o nome do cliente

R : Neste caso verifique o **tamanho do campo** no Protheus e o tamanho do nome que está na receita Federal. Se o tamanho do campo no Protheus for menor que o nome do cliente na receita federal o sistema não preencherá o conteúdo (não apresentará nenhuma mensagem, apenas deixará de preencher)

12) Neste caso de não preencher, o que posso fazer ?

R : Continuando o exemplo do campo Nome (A1\_NOME), é possível digitar manual no campo ou aumentar o tamanho do campo no Configurador.  
  
Este campo em específico não possui grupo de campos, logo, será necessário ao aumentar o tamanho pelo configurador manualmente e validar em base teste.

13) Após a mudança de uso da rotina mata030 para o crma980, a API Carol não funciona.

Para o correto funcionamento da API Carol na nova rotina crma980 é preciso ativar o parâmetro **mv\_mvcsa1 para .**T., mesmo para os casos onde a rotina foi incluída diretamente no menu do SIGAFAT, para que o sistema passe a ler a rotina crma980 corretamente , e deixar de considerar o mata030, que encontra-se descontinuado desde 04/04/22 para as releases 12.1.27 e 12.1.33.

**Obs. Somente a partir da nova release 12.1.2210, quando não haverá mais a chamada da rotina mata030 no menu de faturamento e sim a rotina crma980, que não será mais necessário a ativação do parâmetro mv\_mvcsa1.**

Procure realizar testes nas rotinas padrões, customizadas e relatórios utilizadas pela empresa que retornam o nome do cliente ao digitar o código para evitar possíveis erros de estouro de tamanho de campo
