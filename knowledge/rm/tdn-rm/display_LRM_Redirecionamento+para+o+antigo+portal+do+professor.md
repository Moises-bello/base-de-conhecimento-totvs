---
content_hash: 2c084c96c9f98dfb6ddc7f2db9f83acb744aab68e9c93c5c0d9570067e4842fc
fetched_at: '2026-06-29T00:10:51.607817+00:00'
page_id: '569480745'
product: rm
source: tdn-rm
title: Redirecionamento para o antigo portal do professor
type: documentation
url: https://tdn.totvs.com/display/LRM/Redirecionamento+para+o+antigo+portal+do+professor
version: 27
---

O novo Portal do Professor conta com um recurso que, após a autenticação do usuário, permite o redirecionamento automático para o antigo portal (Corpore.Net), sempre que for acessado um menu que ainda não foi migrado. Dessa forma, não será necessária uma nova autenticação no portal antigo.

Este recurso é válido **apenas do Novo Portal do Professor para o portal antigo (Corpore.Net)**, não sendo aplicável no sentido contrário.

Uma vez definido o contexto no Novo Portal do Professor, ao selecionar um item de menu que ainda não foi migrado, o sistema realizará o redirecionamento automático para o portal antigo, já com as seguintes informações preenchidas: **Coligada, Filial, Nível de Ensino, Código do Sistema e Tipo de Usuário**.

**Observação:** Os filtros escolhidos no Novo Portal, como **Turmas** e **Período Letivo**, não serão refletidos no portal antigo.

Parametrização

A parametrização do redirecionamento para o **Corpore.Net** pode ser realizada de duas formas:

1. **Configuração via `config.json`**

   * É necessário informar a URL do **Corpore.Net** no arquivo `config.json`, na chave `"urlCorpore"`.
   * O arquivo está localizado em: **....FrameHTML\web\app\Edu\portaldoprofessor\config**

**Via TOTVS Gestão Educacional**

* Acessar: **Totvs Gestão Educacional | Ambiente | Parâmetros | Parâmetros Globais | Gerais | URL de acesso ao Portal RM**.
* No campo **URL de acesso ao Portal RM**, especificar o endereço do **Corpore.Net**, no formato: [http://SERVIDOR/NOMEAPLICATIVO\_CORPORE.NET/](http://servidor/NOMEAPLICATIVO_CORPORE.NET/) (Exemplo: <http://servidor/corpore.net/>)

Ocorreu um erro durante o redirecionamento

Caso o **RM.Host.Service** vinculado ao Novo Portal do Professor seja diferente do utilizado no **Corpore.Net**, é obrigatório que as configurações de **Segurança** e **API** sejam idênticas.  
Isso é necessário porque o redirecionamento depende da validação do **token de segurança de integração** gerado.

⚠️ Se as configurações estiverem divergentes, poderá ocorrer o erro: Ocorreu um erro durante o redirecionamento.

### Para dúvidas relacionadas à configuração, verificar:

Lista de recursos ainda não migrados

As funcionalidades do **menu Diário de Classe** que ainda não foram migradas para o Novo Portal do Professor permanecem disponíveis na lista de ações da tela. Ao selecionar um desses itens, o sistema exibirá uma notificação informando que o usuário será redirecionado automaticamente para o **portal antigo do Professor (Corpore.Net)**.

**Itens ainda não migrados:**

* Reserva de Recurso
* Reserva de Instalação
* Complementos das Disciplinas
* **Arquivos da Instituição** **(Disponível a partir da versão: 12.1.2506.276)**
Funcionalidade de Competências/Habilidades

Além disso, estará disponível a funcionalidade **Competências/Habilidades**, restrita ao **Nível de Ensino Básico**.
