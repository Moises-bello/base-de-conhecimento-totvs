---
content_hash: 07f6639442a601d812d9446107ce860d8046ecda571ba210e2c33b38a0ff7428
fetched_at: '2026-06-29T00:05:47.181689+00:00'
page_id: '1008229211'
product: rm
source: tdn-rm
title: Exportação de Ambientes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1008229211
version: 4
---

# O que é?

A Exportação de Ambientes do TOTVS Automação de Testes é uma funcionalidade que permite compartilhar variáveis e configurações dos Ambientes de Execução entre diferentes bases locais ou instalações da ferramenta.

Com ela, é possível gerar um arquivo compactado (.zip) contendo um ou mais ambientes completos, incluindo todas as configurações necessárias para a execução de testes automatizados.  
Esse arquivo pode ser posteriormente importado em outro ambiente, garantindo consistência, compatibilidade e padronização entre execuções.

# Para que serve?

A Exportação de Ambientes foi desenvolvida para facilitar o compartilhamento e a padronização de configurações de execução, reduzindo erros manuais e otimizando o processo de implantação.

Com essa funcionalidade, você pode:

* Mover ambientes configurados entre diferentes bases de dados ou instalações da ferramenta;
* Compartilhar ambientes com outros usuários da equipe;
* Garantir condições idênticas de execução em diferentes ambientes (homologação, produção, filial, etc.);
* Evitar retrabalho, reaproveitando configurações já existentes.

# Exemplo de Uso

Como cadastrarComo Utilizar1- Navegação para Exportar 

 1. Navegue no menu do TOTVS Automação de Testes e clique em **Ambientes.**

 2. Na tabela exibida, selecione os Ambientes que deseja exportar e clique no botão **Exportar** para gerar o arquivo .**zip** contendo todos os ambientes selecionados.

 3. Ao clicar no botão **Exportar**, será exibida uma janela de confirmação que permite escolher se deseja **descaracterizar (ocultar)** os valores das variáveis de ambiente antes da exportação. Essa opção serve para proteger informações confidenciais, como senhas e tokens, garantindo que o arquivo gerado não contenha dados sensíveis.

 Após confirmar, o sistema iniciará o processo de exportação e fará o download automático do arquivo `.zip` gerado.

*Exemplo utilizando todos os Ambientes selecionados*

*Exemplo utilizando Ambientes especificos selecionados*

Exemplo práticoExemplo prático

## Exemplo prático:

## **Cenário: Compartilhamento ou reutilização de ambientes após a importação de projetos de teste**

Quando a equipe de testes precisa replicar a mesma configuração de um ambiente em outra instância do TOTVS Automação de Testes (por exemplo, de homologação para produção ou entre filiais), a exportação permite gerar um pacote portátil do ambiente.

**Para que fazer isso:**  
Essa funcionalidade facilita o compartilhamento e a reutilização de ambientes, garantindo que as variáveis estejam configuradas de forma padronizada, sem necessidade de reconfiguração manual.

---

# Saiba mais

Sempre que exportar projetos de teste, verifique também se o ambiente relacionado foi exportado.

Ao exportar, utilize a opção de descaracterizar variáveis para ocultar senhas e tokens. Armazene os arquivos gerados apenas em locais seguros.

# FAQ

**P: Quando devo usar a Exportação de Ambientes?**

R: Para compartilhar configurações entre diferentes bases ou instalações do TOTVS Automação de Testes; para migrar ambientes entre filiais ou entre homologação e produção; e para reaproveitar configurações já existentes em novos projetos ou contextos.

**P: O que acontece se eu exportar um ambiente com variáveis duplicadas?**

R: A exportação será concluída normalmente. Durante a importação, o sistema identificará os conflitos e exibirá as variáveis duplicadas, ignorando as que já existirem no ambiente de destino.
