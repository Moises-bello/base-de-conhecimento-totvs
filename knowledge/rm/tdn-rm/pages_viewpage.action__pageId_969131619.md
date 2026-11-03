---
content_hash: 31f0534b5420964d172023408408b8d41c84d9eeebf7fa6e60e4afb1acbd033b
fetched_at: '2026-06-29T00:12:14.640297+00:00'
page_id: '969131619'
product: rm
source: tdn-rm
title: Acelerador de Implantação PDC - Criação de Usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=969131619
version: 5
---

O processo de **manutenção de usuários** possibilita a criação automatizada de usuários de acesso ao Portal de Imóveis, ao PDC e ao app Meu Imóvel.

| Após a execução desta funcionalidade, os usuários listados no log deste processo terão o campo *código usuário de acesso*preenchidos no seu cadastro de cliente/fornecedor. |
| --- |

## **Funcionalidades**

* **Usuário de Origem:** Usuário que será utilizado com o "modelo" para que os usuários criados sigam as mesmas configurações de perfis e permissões de acesso.
* **Usuários dos Compradores / Locatários:**
  + **Somente Cli/For sem Usuário:**Ao marcar esta opção, o processo criará códigos de acesso apenas para os usuários que ainda não possuem essa informação preenchida. Essa opção vem selecionada por padrão para evitar que Cli/For já parametrizados sejam processados novamente, prevenindo alterações indesejadas nos seus acessos. Além disso, essa configuração melhora significativamente a performance da execução, pois o sistema processa apenas os usuários nessas condições específicas. Na primeira execução, é comum que todos os Cli/For não possuam usuários cadastrados, mas nas execuções seguintes, haverá um ganho substancial de desempenho.  
    Por outro lado, ao desmarcar essa opção, o sistema processará todos os cadastros, independentemente da situação, o que pode comprometer a performance.
  + **Compradores/Locatários Principal**: Com o parâmetro marcado será criado o usuário apenas para o Comprador/Locatário Principal. Caso esteja desmarcado é criado um usuário considerando os demais compradores/Locatários.
  + **Código de Acesso:** Código de acesso a ser considerado para o banco de dados;
  + **Situação da venda:** Permite selecionar para qual situação de venda irá executar o processo e gerar os usuários. Por padrão, vem selecionada a situação "Efetivada".
  + **Código da Função:** Selecione a função para filtrar para quais grupos de locatários/lojistas serão criados os usuários de acesso. Este campo não é obrigatório e ao deixá-lo em branco, o sistema irá criar e atribuir o usuário de acesso ao cadastro deste cliente/fornecedor;
* **Enviar e-mail para usuários criados:** Se marcada esta opção, irá enviar um e-mail para cada usuário gerado pelo processo, informando a criação do usuário, seu código de acesso e sua senha.
  + **Endereço de acesso ao portal**: Este campo deverá ser preenchido e será considerado no e-mail enviado. Ele deve conter o caminho do portal a ser acessado, para que os compradores saibam qual o link de acesso. Este campo, após o primeiro preenchimento, virá preenchido nas próximas vezes em que o usuário executar o processo.
  + **Assunto do E-mail**: Ao informar será enviado o assunto preenchido no processo, caso o campo fique sem preenchimento o irá enviar no assunto o texto '**Acesso ao portal do cliente**'.
