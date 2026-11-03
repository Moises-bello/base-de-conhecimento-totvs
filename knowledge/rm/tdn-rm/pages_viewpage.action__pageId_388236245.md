---
content_hash: 639bc33801ebc999699cdf625adce18f5171f483b54856dcd5c6775bda03b2f6
fetched_at: '2026-06-29T00:09:08.418241+00:00'
page_id: '388236245'
product: rm
source: tdn-rm
title: Como discriminar nos eventos S-1200 e S-1210 a Tag <ideDmDev> para funcionários
  com categorias diferentes?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=388236245
version: 6
---

**Prefixo Período (eSocial)**

Utilize esta informação para que no momento da geração dos eventos S-1200 e S-1210 os eventos possam ser separados por funcionário que tem múltiplos vínculos e os mesmos têm lançamentos no mesmo período de pagamento. Este campo aceita até 10 caracteres.

 A informação está disponível no cadastro de funcionários na pasta Parãmetros após a execução de script de atualização da base de dados.

**ATENÇÃO:** O script a ser executado se encontra em <https://suporte.totvs.com/portal/p/10098/download#detail/701342>

Em cada cadastro deste campo será informado um valor, para o exemplo será utilizado a chapa do funcionário.

**Funcionário código da Pessoa 1 - categoria 101 – chapa 00001**

**Diretor código da Pessoa 1 - categoria 721 – chapa 77777**

No momento da geração do xml será informado na Tag <ideDmDev> será informada da seguinte forma:

 Para o Diretor categoria 101

<ideDmDev>100001<\ideDmDev>

 Para o Funcionário categoria 721

<ideDmDev>177777<\ideDmDev>

**S- 1200**

**S- 1210**

**Observações:** A informação da Tag <ideDmDev>.será a união do período com a informação do campo no cadastro de funcionários. Caso o campo não seja preenchido somente o número do período será informado na Tag <ideDmDev>.

                      O campo pode ser preenchido com números ou letras.
