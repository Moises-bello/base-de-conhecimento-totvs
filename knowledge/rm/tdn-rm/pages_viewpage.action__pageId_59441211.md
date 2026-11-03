---
content_hash: 2d54f3b086d3fbf2be7f0f4447fe36d4813a89ada67e4b25688e4813c1bcb814
fetched_at: '2026-06-29T00:10:57.110582+00:00'
page_id: '59441211'
product: rm
source: tdn-rm
title: Inclusão de MAPAS em anexos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=59441211
version: 12
---

# Índice

---

# Parametrizando a API do Google e configurando o RM.

---

Para parametrizar a API do Google e configurar o RM, acesse a documentação: 

# Utilizando Mapas em Anexos

---

Mapas podem ser utilizados em telas que possuem endereço no sistema, ou através de uma consulta SQL que retorne um endereço para o registro da tela.

Após inserir uma Chave de Identificação válida no RM, conforme feito no documento anterior, já é possível utilizar o recurso de Mapas no RM.

Primeiramente, acesse a tela deseja. Neste exemplo usaremos o cadastro de Clientes/Fornecedores.

1) Acesse: Anexos > Mapa > Inserir Anexo.

2) Informe uma descrição do processo para o Mapa e clique em avançar:

3) Insira o nome do Anexo e clique em avançar.

Obs.: Se os parâmetros de endereço forem disponibilizados por uma Consulta SQL, selecione a opção e marque a consulta desejada.

4) Na tela seguinte informe os parâmetros para a busca do endereço no Mapa.

Não é necessário preencher todos os campos, mas são necessários os mais importantes para a busca de um endereço.

5) Defina os usuários/perfis que terão acesso a consulta destes mapas.

No exemplo abaixo a opção 'Todos' permite que todos os usuários do sistema tenham acesso.

6) Clique em 'Executar' para finalizar a parametrização do anexo.

7) Para visualizar o Mapa em anexos, acesse: Anexos > Mapas > Mapa Cli-For.

Após a tela de anexos ser carregada, basta selecionar o registro que será carregado.

Ao navegar nos registros automaticamente o mapa será atualizado.

Obeservações:

O Parâmetro Global URL de acesso ao Portal RM **deve** ser preenchido com o **IP do Portal** e **não** o Hostname.

**Obs.: O serviço de APIs do Google Maps não é gratuito!**

Veja mais detalhes na documentação: .

Se após a configuração do Anexo de Mapas o RM retornar alguma das mensagens de erro abaixo, favor verificar junto a sua conta Google se as requisições contratadas estão dentro do limite e se o contrato está ativo.

Primeira possibilidade de erro:

Segunda possibilidade de erro:

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Incluir Anexo de Mapas
